LET HEIGHT = 5

FOR I = 1 TO HEIGHT
    FOR J = 1 TO HEIGHT - I
        PRINT " ";
    NEXT J
    FOR K = 1 TO 2 * I - 1
        PRINT "*";
    NEXT K
    PRINT ""
NEXT I
FOR L = 1 TO HEIGHT - 1
    PRINT " ";
NEXT L
PRINT "*"