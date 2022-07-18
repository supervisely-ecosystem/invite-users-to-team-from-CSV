<div align="center" markdown>

<img src="https://i.imgur.com/3Ty8mqK.png"/>

# Invite users to team from CSV

<p align="center">

  <a href="#Overview">Overview</a> •
  <a href="#Preparation">Preparation</a> •
  <a href="#How-To-Run">How To Run</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/invite-users-to-team-from-csv)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/invite-users-to-team-from-csv)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/invite-users-to-team-from-csv)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/invite-users-to-team-from-csv)](https://supervise.ly)

</div>

## Overview

This app allows to invite multiple users to team in a few clicks. Is saves time especially if you have large labeling team or annotators, managers and developes that are distributed accross regions and countries. User have to define CSV files with logins and roles in team and then these CSV files are used to bulk-invite members. 

For example, you can create several files: `manages_new_york.csv`, `developers_moscow.csv`, `labelers_san_francisco.csv`, `labelers_new_delhi.csv` and so on. Then you can invite different users groups to different teams. We recommend for every research or labeling project create separate team in Supervisely. It allows to keep data, experiments and annotation activity in a consistent way.

## Preparation

List of default roles (detailed explanation of permmissions for each role can be found in [our docs](https://docs.supervise.ly/collaboration/members)):
- `admin`
- `developer`
- `manager`
- `annotator` 
- `viewer`
- `reviewer`

Create a `.csv` file with two columns: `logins` and `roles`, all elements must be separated with `,`. For example:

```
login,role
alex,manager 
cxnt,developer
max,annotator
```

Drag and drop `CSV` file to Team Files

<img src="https://i.imgur.com/SE1s0OF.png"/>



## How To Run 

**Step 1**: Add app to your team from [Ecosystem](https://ecosystem.supervise.ly/apps/invite-users-to-team-from-CSV) if it is not there.

**Step 2**: Go to `Current Team`->`Files` page, right-click on your `CSV` file  and choose `Run App`->`Invite users to team from CSV`. 

<img src="https://i.imgur.com/B1z7Ltf.png"/>


**Step 3**: To see logs go to `Current Team`->`PLugins & Apps` page -> `Application sessions` -> `LOGS` button.  

<img src="https://i.imgur.com/cSaKmoI.png"/>


App log shows invited users or warning messages if user/role doesn't exist or user is already in team.

<img src="https://i.imgur.com/Mg01tRT.png"/>

