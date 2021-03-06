CREATE DATABASE db_bbs;

CREATE TABLE `tbl_user`(
`uid` INT(30) NOT NULL AUTO_INCREMENT,
`username` VARCHAR(20) NOT NULL,
`password` VARCHAR(20) NOT NULL,
PRIMARY KEY (`uid`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `tbl_posts`(
`id` INT(15) NOT NULL AUTO_INCREMENT,
`last_time` INT(12) NOT NULL,
`tag` TINYBLOB NOT NULL,
`content` BLOB NOT NULL,
`comment` BLOB NOT NULL,
PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `tbl_role`(
`uid` INT(15) NOT NULL AUTO_INCREMENT,
`rid` INT(12) NOT NULL,
`posts` TINYBLOB NOT NULL,
`comment` TINYBLOB NOT NULL,
PRIMARY KEY (`uid`,`rid`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;