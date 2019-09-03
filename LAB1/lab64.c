#include <unistd.h>
#include <sys/types.h>
main()
{
pid_t pid,pid1;
int n;
printf("Enter number of forks\n");
scanf("%d",&n);
printf("just one process before the fork() \n");

for(int k=0;k<n;k++){
pid= fork();
int  i,j;
i=getpid();
j=getppid();
printf("------------------------\n");
printf("curr=%d, parent=%d\n",i,j);
if(pid == 0)
printf("I am the child process %d\n",k+1);
else if(pid > 0)
printf("I am the parent process %d\n",k+1);
else
printf("The fork() has failed \n");
  }


/*pid1=fork();
int  a,b;
a=getpid();
b=getppid();
printf("----------------------\n");
printf("curr=%d, parent=%d\n",a,b);
if(pid1==0)
printf("I am the child process 2\n");
else if(pid1>0)
printf("I am the parent process 2\n");
else
printf("The fork() has failed\n");*/


}