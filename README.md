<div align="center" markdown>

# Invite users to team from CSV


<p align="center">

  <a href="#Overview">Overview</a> •
  <a href="#Preparation">Preparation</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#How-To-Use">How To Use</a>
</p>

[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/remote-import)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/remote-import&counter=views&label=views)](https://supervise.ly)
[![used by teams](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/remote-import&counter=downloads&label=used%20by%20teams)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/remote-import&counter=runs&label=runs&123)](https://supervise.ly)

</div>

## Overview

Application invite users with given roles to current team from CSV format.



## Preparation

1. Create a `.csv` file with `logins` and `roles`
2. `.csv` file must contain only 2 columns: `login` and `role`, all elements must be separated with `,`
3. Here's the example of how your `.csv` file should look like:

```
login, role
user1, annotator 
user2, reviewer
user3, annotator
user4, jobmanager
max, admin
```

4. Drag and drop this file to Team Files



<img src="https://i.imgur.com/TEpBMXf.gif"/>



## How To Run 
**Step 1**: Add app to your team from Ecosystem if it is not there. Application will be added to `Current Team`->`PLugins & Apps` page. 

<img src="https://i.imgur.com/8olwkGI.png"/>



**Step 2**: Go to `Current Team`->`Files` page, right-click on your `.csv file` and choose `Run App`->`Invite users to team from CSV`. 

<img src="https://i.imgur.com/Y1TgrkG.png"/>



**Note**: To open log go to `Current Team`->`PLugins & Apps` page. 


## How to use

1. Check project you want to convert to yolo5 format.

2. Click three point on project and choise "Download as" option.

3. In popup menu choise "Convert Supervisely into YOLO v5 format".

<img src="https://i.imgur.com/ZTYhihF.png"/>

4. Open "files" menu. Here in directory "yolov5_format" you can find tar archive with project in YOLOv5 format.

<img src="https://i.imgur.com/pu9snon.png"/>



