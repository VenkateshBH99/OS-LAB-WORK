#include<unistd.h>
#include<sys/types.h>
int main(){
	pid_t pid;
	int n;
	printf("Enter n:\n");
	scanf("%d",&n);
	pid=fork();
	if(pid==0)
	{
		int temp=1;
		for(int i=2;i<=n;i++){
			temp*=i;
		}
		printf("factorial=%d\n",temp );
	}
	else if(pid<0){
		printf("process failed!!\n");
	}
	

}