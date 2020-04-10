CREATE TABLE `user_info` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `login_name` varchar(64) NOT NULL COMMENT '登录名',
  `password_hash` varchar(255) NOT NULL DEFAULT '' COMMENT '密码哈希',
  `user_nation` varchar(255) DEFAULT NULL COMMENT '用户国家',
  `user_province` varchar(255) DEFAULT NULL COMMENT '用户省份',
  `user_city` varchar(255) DEFAULT NULL COMMENT '用户城市',
  `user_zone` varchar(255) DEFAULT NULL COMMENT '用户地区',
  `user_address` varchar(255) DEFAULT NULL COMMENT '用户地址',
  `user_school` varchar(255) NOT NULL COMMENT '用户学校',
  `user_weibo` varchar(255) DEFAULT NULL COMMENT '用户微博',
  `user_mail` varchar(255) DEFAULT NULL COMMENT '用户邮箱',
  `user_qq` varchar(255) DEFAULT NULL COMMENT '用户QQ',
  `user_wechat` varchar(255) DEFAULT NULL COMMENT '用户微信',
  `user_avatar` varchar(255) DEFAULT NULL COMMENT '用户头像',
  `user_gender` tinyint(2) DEFAULT NULL COMMENT '用户性别 1 男 ,2 女,3 未知',
  `user_birthday` date DEFAULT NULL COMMENT '用户生日',
  `user_statement` varchar(255) DEFAULT NULL COMMENT '用户签名',
  `user_background_url` varchar(255) NOT NULL COMMENT '用户背景URL',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_info_login_name` (`login_name`),
  KEY `ix_user_info_user_mail` (`user_mail`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;


INSERT INTO `app`.`user_info`(`id`, `login_name`, `password_hash`, `user_nation`, `user_province`, `user_city`, `user_zone`, `user_address`, `user_school`, `user_weibo`, `user_mail`, `user_qq`, `user_wechat`, `user_avatar`, `user_gender`, `user_birthday`, `user_statement`, `user_background_url`, `create_time`, `update_time`) VALUES (4, 'superman', '', '中国', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '2020-04-02 08:03:43', '2020-04-02 08:07:51');
INSERT INTO `app`.`user_info`(`id`, `login_name`, `password_hash`, `user_nation`, `user_province`, `user_city`, `user_zone`, `user_address`, `user_school`, `user_weibo`, `user_mail`, `user_qq`, `user_wechat`, `user_avatar`, `user_gender`, `user_birthday`, `user_statement`, `user_background_url`, `create_time`, `update_time`) VALUES (5, 'hc', 'e10adc3949ba59abbe56e057f20f883e', NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '2020-04-03 08:15:26', '2020-04-04 15:19:41');
INSERT INTO `app`.`user_info`(`id`, `login_name`, `password_hash`, `user_nation`, `user_province`, `user_city`, `user_zone`, `user_address`, `user_school`, `user_weibo`, `user_mail`, `user_qq`, `user_wechat`, `user_avatar`, `user_gender`, `user_birthday`, `user_statement`, `user_background_url`, `create_time`, `update_time`) VALUES (6, '小明', '123456', '中国', NULL, NULL, NULL, NULL, '', NULL, 'xm@163.com', NULL, NULL, NULL, 1, '2020-04-08', NULL, '', '2020-04-04 15:20:56', '2020-04-04 15:20:56');