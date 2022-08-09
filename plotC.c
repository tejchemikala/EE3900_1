#include<stdio.h> 
int main()
{
    FILE *fp;
    fp =fopen("Ydata.txt", "w");
    if(fp==NULL) printf("file opening failed");
    float x[6] = {1.0,2.0,3.0,4.0,2.0,1.0};
    for(int i=0 ;i<6;i++) fprintf(fp,"%f ",x[i]);
    fprintf(fp,"\n");
    float y[20];
    int k =20;
    y[0]=x[0];
    y[1] =  (-0.5*y[0]) + x[1];
    for(int i=2;i<k-1;i++)
    {
        if(i<6) y[i] = -0.5*y[i-1] + x[i] + x[i-2];
        else if(i>5 && i<8) y[i] = -0.5*y[i-1] + x[i-2];
        else y[i] = -0.5*y[i-1];
    }
    //fputs(y,fp);
    for(int i=0;i<k;i++)
    {
        fprintf(fp,"%f ",y[i]);
        //printf("%f  ",y[i]);
    
    }
    fprintf(fp,"\n");

}
