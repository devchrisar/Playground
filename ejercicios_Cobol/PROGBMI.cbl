       IDENTIFICATION DIVISION.
       PROGRAM-ID. "PROGBMI".
       AUTHOR.     DEVCHRISAR.
       *>--------------------------------------------------------------*                                       
       *>    CALCULAR Y MOSTRAR EL BMI DEL USUARIO                     *
       *>--------------------------------------------------------------*
       ENVIRONMENT DIVISION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WEIGHT PIC 999.
       01 HEIGHT_INCHES PIC 999.
       01 BMI PIC Z99.99.

       PROCEDURE DIVISION.
       0100-INICIO.
       DISPLAY "DIGITE SU ALTURA EN CENTIMETROS :".
       ACCEPT HEIGHT_INCHES.
       DISPLAY "DIGITE SU PESO EN KILOGRAMOS :".
       ACCEPT WEIGHT.
       COMPUTE BMI = WEIGHT / HEIGHT_INCHES / HEIGHT_INCHES * 10000.
       *>--------------------------------------------------------------*
       *>      VERSION CON SISTEMA INGLES (PULGADAS Y GRAMOS)          *
       *> COMPUTE BMI = WEIGHT * 703 / (HEIGHT_INCHES * HEIGHT_INCHES).*
       *>--------------------------------------------------------------*
       DISPLAY "TU BMI ES :",BMI,"%".

       STOP RUN.
       END PROGRAM PROGBMI.
       
