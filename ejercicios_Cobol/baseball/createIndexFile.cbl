       IDENTIFICATION DIVISION.
       PROGRAM-ID. CREATEINDEXFILE.
      *> CREATE AN INDEXED FILE FROM A SEQUENTIAL FILE
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.

	   SELECT BASEBALLSEQ ASSIGN TO "BASEBALL2016.NEW"
	     ORGANIZATION IS LINE SEQUENTIAL.
       
       SELECT BASEBALLIDX ASSIGN TO "BASEBALLIDX.DAT"
        FILE STATUS IS FILE-CHECK-KEY
		ORGANIZATION IS INDEXED
		ACCESS MODE IS RANDOM
		RECORD KEY IS CODEIDX
		ALTERNATE RECORD KEY IS DATE-IDX
		   WITH DUPLICATES
        ALTERNATE RECORD KEY IS HOME-TEAMIDX
             WITH DUPLICATES.

       DATA DIVISION.
       FILE SECTION.
	   FD BASEBALLIDX.
	   01 BASEBALLRECORDIDX.
	      05 CODEIDX         PIC X(36).
          05 FILLER          PIC X(4).
		  05 DATE-IDX        PIC X(10).
          05 FILLER          PIC X(18).
          05 AWAY-TEAMIDX    PIC X(12).
          05 HOME-TEAMIDX    PIC X(12).
          05 FILLER          PIC X(34).
	
       FD BASEBALLSEQ.
	   01 BASEBALLRECORDSEQ.
	      88 ENDOFFILE      VALUE HIGH-VALUES.
          02 IN-RECORD          PIC X(127).
          02 IN-DETAIL-RECORD REDEFINES IN-RECORD.
	      05 IN-CODESEQ         PIC X(36).
          05 IN-YR              PIC 9(4).
		  05 IN-DATESEQ.
             10 IN-YEAR         PIC 9999.
             10 FILLER          PIC X.
             10 IN-MONTH        PIC 99.
             10 FILLER          PIC X.
             10 IN-DAY          PIC 99.
          05 FILLER             PIC X.
          05 IN-START-TIME      PIC X(8).
          05 FILLER             PIC X.
          05 IN-TIMEZONE        PIC X(3).
          05 IN-ATTENDANCE      PIC 9(5).
          05 IN-HOME-TEAM       PIC X(12).
		  05 IN-AWAY-TEAM       PIC X(12).
          05 IN-VENUE           PIC X(20).
          05 IN-STATE           PIC X(2).
          05 IN-HOME-SCORE      PIC 9(2).
          05 IN-AWAY-SCORE      PIC 9(2).
          05 IN-INNING          PIC 9(2).
          05 IN-STATUS          PIC X(6).
	
		
       WORKING-STORAGE SECTION.
       01  WS-WORKING-STORAGE.
           05 FILLER      PIC X(27) VALUE 
		      'WORKING STORAGE STARTS HERE'.
   
	   01  WS-WORK-AREAS.
	       05  FILE-CHECK-KEY     PIC X(2).

       PROCEDURE DIVISION.
       0100-READ-BASEBALL-GAMES.

		   OPEN INPUT BASEBALLSEQ.
		   OPEN OUTPUT BASEBALLIDX.
		   				
           READ BASEBALLSEQ 
		     AT END SET ENDOFFILE TO TRUE
		   END-READ.
		   PERFORM 0200-PROCESS-FILE UNTIL
		      ENDOFFILE.
		 
		   PERFORM 9000-END-PROGRAM.
		   
	   0100-END.
	   
	   0200-PROCESS-FILE.
	  
		   WRITE BASEBALLRECORDIDX FROM BASEBALLRECORDSEQ
		      INVALID KEY DISPLAY 
			     "BASEBALL FILE STATUS = " FILE-CHECK-KEY
		   END-WRITE.
		   READ BASEBALLSEQ
		      AT END SET ENDOFFILE TO TRUE.
		0200-END.
		   
	   9000-END-PROGRAM.
           CLOSE BASEBALLSEQ, BASEBALLIDX. 
           STOP RUN.
           
          END PROGRAM CREATEINDEXFILE.
