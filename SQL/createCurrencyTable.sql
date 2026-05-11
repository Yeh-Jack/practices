
CREATE TABLE IF NOT EXISTS `taiwanbank_currency` (
  `date` datetime DEFAULT NULL,
  `currency` varchar(50) DEFAULT NULL,
  `buy` decimal(20,6) DEFAULT NULL,
  `sold` decimal(20,6) DEFAULT NULL
);
