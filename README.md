<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="assets\icons\Robot_arm_log.png" alt="Project logo"></a>
</p>

<h3 align="center">比邻星科技六轴机械臂</h3>

<div align="center">

<!-- [![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls) -->
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 能写字、跳舞的六轴机械臂.
    <br> 
</p>

## 📝 Table of Contents

- [关于](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 关于 <a name = "about"></a>

比邻星六轴机械臂

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### MDH 参数

| 关节 | alpha   | a | d      | theta   |
| ---- |---------| -- |--------|---------|
| 1 | 0       | 0 | 143.5  | 0       |
| 2 | -pi / 2 | 0 | 0      | -pi / 2 |
| 3 | 0       | 160.72 | 0      | 0       |
| 4 | -pi / 2 | 0 | 238.37 | 0       |
| 5 | pi / 2  | 0 | 0      | pi/2    |
| 6 | pi / 2  | 0 | -70.79 | 0       |

## 机械臂电机方向与角度范围

> 先将屏幕面向操作者，将机械臂回零，再确定电机的角度正负值，以及对应的控制方向
>
> 需要与正逆解模型的角度方向一致

| 电机编号 | 方向   | 负值（度） | 正值(度) | 方向   | 备注 |
| -------- | ------ | ---------- | -------- | ------ | ---- |
| 1        | 顺时针 | -140       | +140     | 逆时针 | 俯视 |
| 2        | 顺时针 | -70        | +70      | 逆时针 | 左视 |
| 3        | 顺时针 | -60        | +45      | 逆时针 | 左视 |
| 4        | 逆时针 | -150       | +150     | 顺时针 | 正视 |
| 5        | 顺时针 | -180       | +10      | 逆时针 | 左视 |
| 6        | 顺时针 | -180       | +180     | 逆时针 | 俯视 |

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
