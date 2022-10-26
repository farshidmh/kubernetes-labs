<link rel='stylesheet' href='../../assets/css/main.css'/>

# Lab: Let's Deploy Some Classic Games

## Overview

In this lab, we are going to deploy some classic gems : **Pacman and Mario**

## Duration

20 mins

## Step-1: Run the Games Locally

Luckily for us, these classic games are dockerized, so we can run them on our local machines!

### Pacman

https://hub.docker.com/r/golucky5/pacman

```bash
    $   docker pull golucky5/pacman
    $   docker run -d --rm -p 8000:80 golucky5/pacman
```

http://localhost:8000

### Super Mario

https://hub.docker.com/r/pengbai/docker-supermario

```bash
    $   docker pull pengbai/docker-supermario
    $   docker run -d --rm -p 8001:8080 pengbai/docker-supermario
```

Go to :  http://localhost:8001

## Step-2: Deploy These Games

Use [canary deployment](../../deployments/canary/README.md) to deploy both games.

Users will randomly get Pacman or Mario!

Start working from the [canary deployment lab files](../../deployments/canary/)

## Step-4: Demo to the Class!

Let's have some fun and end the class with some video games!