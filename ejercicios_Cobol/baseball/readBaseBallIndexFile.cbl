       IDENTIFICATION DIVISION.
       PROGRAM-ID. READINDEXFILE.
      *> READS AN INDEXED FILE 
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
	   
	   SELECT BASEBALL ASSIGN TO "BASEBALLIDX.DAT"
        FILE STATUS IS FILE-CHECK-KEY
		   ORGANIZATION IS INDEXED
		   ACCESS MODE IS DYNAMIC
		   RECORD KEY IS CODEIDX
           ALTERNATE RECORD KEY IS DATE-IDX
		     WITH DUPLICATES
           ALTERNATE RECORD KEY IS HOME-TEAMIDX
             WITH DUPLICATES.
		   
       DATA DIVISION.
       FILE SECTION.
	   FD BASEBALL.
	   01 BASEBALLRECORDIDX.
          88 ENDOFFILE       VALUE HIGH-VALUES.
	      05 CODEIDX         PIC X(36).
          05 FILLER          PIC X(4).
		  05 DATE-IDX        PIC X(10).
          05 FILLER          PIC X(13).
		  05 ATTENDANCE      PIC 99999.
          05 AWAY-TEAMIDX    PIC X(12).
          05 HOME-TEAMIDX    PIC X(12).
          05 FILLER          PIC X(35).

       WORKING-STORAGE SECTION.
       01  WS-WORKING-STORAGE.
           05 FILLER               PIC X(27) VALUE 
		      'WORKING STORAGE STARTS HERE'.    
   
	   01  WS-WORK-AREAS.
	       05  FILE-CHECK-KEY      PIC X(2).
		       88 RECORDFOUND      VALUE "00".
			   
		   05  READTYPE            PIC 9.
		       88 CODE-KEY         VALUE 1.
			   88 DATE-KEY         VALUE 2.
               88 HOME-TEAM-KEY    VALUE 3.
               88 READ-ALL-KEY     VALUE 4.
		   05  WS-DATE             PIC X(10).
           05  WS-HOME-TEAM        PIC X(12).

       PROCEDURE DIVISION.
       0100-START.

		   OPEN INPUT BASEBALL.
		   DISPLAY "SELECT RECORD BY BASEBALL CODE, ENTER 1". 
		   DISPLAY "SELECT RECORD BY DATE (YYYY-MM-DD), ENTER 2".
           DISPLAY "SELECT RECORD BY HOME TEAM NAME, ENTER 3".
           DISPLAY "DISPLAY ALL RECORDS, ENTER 4".
			  
		   ACCEPT READTYPE.
		   
		   IF CODE-KEY 
		      DISPLAY "ENTER BASEBALL CODE KEY (36 DIGITS): " 
			    WITH NO ADVANCING		    
			  ACCEPT CODEIDX
			  READ BASEBALL
			    KEY IS CODEIDX
			    INVALID KEY DISPLAY "BASEBALL FILE STATUS: ",
				  FILE-CHECK-KEY
			  END-READ			 
           END-IF.	

           IF DATE-KEY
		      DISPLAY "ENTER DATE: (YYYY-MM-DD): " 
			    WITH NO ADVANCING
			  ACCEPT DATE-IDX
              MOVE DATE-IDX TO WS-DATE
              READ BASEBALL 
                 KEY IS DATE-IDX
                 END-READ
               DISPLAY BASEBALLRECORDIDX
              PERFORM 0200-READ-NEXT-DATE THRU 0200-END
                 UNTIL ENDOFFILE
            END-IF.

           IF HOME-TEAM-KEY
		      DISPLAY "ENTER HOME TEAM NAME: " 
			    WITH NO ADVANCING
			  ACCEPT HOME-TEAMIDX
              MOVE HOME-TEAMIDX TO WS-HOME-TEAM
              READ BASEBALL
                KEY IS HOME-TEAMIDX			  
                END-READ
                DISPLAY BASEBALLRECORDIDX
                PERFORM 0150-READ-NEXT-DATE THRU 0150-END 
                   UNTIL ENDOFFILE
			END-IF.
            
            IF READ-ALL-KEY
               READ BASEBALL 
                 KEY IS HOME-TEAMIDX
                 END-READ
               DISPLAY BASEBALLRECORDIDX
               PERFORM 0300-READ-ALL THRU 0300-READ-ALL-END 
                  UNTIL ENDOFFILE
            END-IF.

		   PERFORM 9000-END-PROGRAM.
		   
	   0100-END.

       0150-READ-NEXT-DATE.
          READ BASEBALL NEXT RECORD
             AT END SET ENDOFFILE TO TRUE
            END-READ. 		  
           IF HOME-TEAMIDX = WS-HOME-TEAM
               DISPLAY BASEBALLRECORDIDX
           END-IF.        
        0150-END. 
       0200-READ-NEXT-DATE.
          READ BASEBALL NEXT RECORD
             AT END SET ENDOFFILE TO TRUE
            END-READ. 		  
           IF DATE-IDX = WS-DATE
               DISPLAY BASEBALLRECORDIDX
           END-IF.        
        0200-END.   

       0300-READ-ALL.
          READ BASEBALL NEXT RECORD
             AT END SET ENDOFFILE TO TRUE
            END-READ. 		  
           IF RECORDFOUND 
               DISPLAY BASEBALLRECORDIDX
           END-IF.        
        0300-READ-ALL-END.
	 
	   9000-END-PROGRAM.
           CLOSE BASEBALL.    	   
		                 
           STOP RUN.
           
          END PROGRAM READINDEXFILE.
