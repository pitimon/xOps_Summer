SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `student` (
  `id` int NOT NULL,
  `FirstName` varchar(255) NOT NULL,
  `LaseName` varchar(255) DEFAULT NULL,
  `Email` varchar(255) NOT NULL
) ENGINE=InnoDB CHARSET=utf8 COLLATE utf8_general_ci;

ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);
  
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;
