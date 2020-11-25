import os
import csv

import supervisely_lib as sly

my_app = sly.AppService()

TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])
INPUT_FILE = os.environ['modal.state.slyFile']

LOGIN_COL_NAME = 'login'
ROLE_COL_NAME = 'role'
DEFAULT_DELIMITER = ','


@my_app.callback("add_users_to_team_from_csv")
@sly.timeit
def add_users_to_team_from_csv(api: sly.Api, task_id, context, state, app_logger):

    storage_dir = my_app.data_dir
    local_csv_path = os.path.join(storage_dir, "group.csv")
    api.file.download(TEAM_ID, INPUT_FILE, local_csv_path)

    possible_roles = api.role.get_list()
    role_to_id = {}
    for curr_role in possible_roles:
        role_to_id[curr_role.role] = curr_role.id

    existing_users = api.user.get_list()
    existing_logins = [user.login for user in existing_users]

    with open(local_csv_path, "r") as f_obj:
        adding_to_team_users = {}
        reader = csv.DictReader(f_obj, delimiter=DEFAULT_DELIMITER)

        for row in reader:
            login = row[LOGIN_COL_NAME].strip()
            role = row[ROLE_COL_NAME].strip()

            if login not in existing_logins:
                app_logger.warn("Login {} not exist".format(login))
                continue

            if role not in role_to_id.keys():
                app_logger.warn("role {} not exist".format(role))
                continue

            if login in adding_to_team_users:
                app_logger.warn('Duplicate login found in csv file: {}'.format(login))
                continue


            adding_to_team_users[login] = role_to_id[role]


    progress = sly.Progress('Adding users to team...', len(adding_to_team_users), app_logger)

    for login, role_id in adding_to_team_users.items():
        if api.user.get_member_info_by_login(TEAM_ID, login):
            app_logger.warn("User with login {} already in team".format(login))
            continue
        api.user.add_to_team_by_login(login, TEAM_ID, role_id)
        app_logger.info("User {!r} is added".format(login))
        progress.iter_done_report()

    sly.fs.silent_remove(local_csv_path)

    my_app.stop()


def main():
    sly.logger.info("Script arguments", extra={
        "TEAM_ID": TEAM_ID,
        "WORKSPACE_ID": WORKSPACE_ID,
        "INPUT_FILE": INPUT_FILE
    })

    # Run application service
    my_app.run(initial_events=[{"command": "add_users_to_team_from_csv"}])


if __name__ == "__main__":
    sly.main_wrapper("main", main)