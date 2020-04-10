#!/bin/sh

echo "开始制作镜像..."
image_tag=`date +%Y%m%d` #_%H%M
echo "当前时间：$image_tag"
docker build -t python36base_tornado:v${image_tag} .
echo "镜像名字如下"
echo python36base_tornado:v${image_tag}
docker python36base_tornado:v${image_tag} python36base_tornado:latest
echo "制作镜像成功!"
