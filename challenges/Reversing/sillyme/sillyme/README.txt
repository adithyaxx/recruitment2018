Problem of this program is a stupid pointer mistake. 
Along the line of


char flag[100] = "";
char *temp = flag;
char char1 = 'H';
char char2 = 'I';

*temp++ = char1;
*temp++ = char2;
*temp++ = char1;
*temp++ = char2;

printf("%s",temp);




Stupid isnt it... Please help me get the flag nonetheless. Thanks
