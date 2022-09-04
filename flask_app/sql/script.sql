-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema proyecto_personal
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema proyecto_personal
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `proyecto_personal` DEFAULT CHARACTER SET utf8 ;
USE `proyecto_personal` ;

-- -----------------------------------------------------
-- Table `proyecto_personal`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_personal`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre_completo` VARCHAR(45) NULL,
  `alias` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `contraseña` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto_personal`.`poemas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_personal`.`poemas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `poema` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_poemas_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_poemas_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `proyecto_personal`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto_personal`.`me_gusta_por_usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_personal`.`me_gusta_por_usuario` (
  `poema_id` INT NOT NULL,
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`poema_id`, `usuario_id`),
  INDEX `fk_poemas_has_usuarios_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  INDEX `fk_poemas_has_usuarios_poemas1_idx` (`poema_id` ASC) VISIBLE,
  CONSTRAINT `fk_poemas_has_usuarios_poemas1`
    FOREIGN KEY (`poema_id`)
    REFERENCES `proyecto_personal`.`poemas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_poemas_has_usuarios_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `proyecto_personal`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
