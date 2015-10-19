CREATE TABLE costumer (
  idcostumer INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(75) NOT NULL,
  register VARCHAR(14) NULL,
  birth DATE NULL
);


-- -----------------------------------------------------
-- Table `pycostumer`.`phone`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pycostumer`.`phone` (
  `number` VARCHAR(20) NOT NULL,
  `label` VARCHAR(20) NOT NULL,
  `fkcostumer` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`number`, `fkcostumer`),
  INDEX `fk_phone_costumer_idx` (`fkcostumer` ASC),
  CONSTRAINT `fk_phone_costumer`
    FOREIGN KEY (`fkcostumer`)
    REFERENCES `pycostumer`.`costumer` (`idcostumer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pycostumer`.`address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pycostumer`.`address` (
  `idaddress` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `fkcostumer` INT UNSIGNED NOT NULL,
  `street` VARCHAR(75) NOT NULL,
  `neighb` VARCHAR(40) NULL,
  `city` VARCHAR(40) NULL DEFAULT 'Divinópolis',
  `state` VARCHAR(2) NULL DEFAULT 'MG',
  `zipcode` VARCHAR(8) NULL,
  `country` VARCHAR(20) NULL DEFAULT 'Brasil',
  PRIMARY KEY (`idaddress`, `fkcostumer`),
  UNIQUE INDEX `idaddress_UNIQUE` (`idaddress` ASC),
  CONSTRAINT `fk_address_costumer`
    FOREIGN KEY (`fkcostumer`)
    REFERENCES `pycostumer`.`costumer` (`idcostumer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
