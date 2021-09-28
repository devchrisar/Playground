       IDENTIFICATION DIVISION.
       PROGRAM-ID. "ObtenerInput".
       AUTHOR.     DEVCHRISAR.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 NOMBRE PIC A(20).
       PROCEDURE DIVISION.
           0100-INICIO.
              DISPLAY "¿COMO TE LLAMAS? :".
              ACCEPT NOMBRE.
              DISPLAY "QUE GUSTO, ",NOMBRE.
       STOP RUN.
       END PROGRAM ObtenerInput.
