#include<stdio.h>
#include<stdlib.h>
int main(){
	FILE *in,*out;
	in=fopen("in.txt","r");
	out=fopen("/home/student/Documents/ou.txt","w");
	if(in==NULL || out==NULL){
		printf("Error! Could not open file\n"); 
              exit(-1);
          }
         char c;
         c=fgetc(in);
         while(c!=EOF){
         	fputc(c,out);
         	c=fgetc(in);
         }
         fclose(in);
         fclose(out);
         return 0;

}