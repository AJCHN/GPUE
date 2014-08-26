#include<assert.h>
#include<cuda.h>
#include<stdio.h>
#include<cuda_runtime.h>
#include"gpu_functions.cu"

void test_scalVectMult(){
        int xDim, yDim;
        xDim=256;
        yDim=256;

        double *v1, *v1_gpu;
        v1 = (double*) malloc(sizeof(double)*xDim*yDim);
        cudaMalloc((void**) &v1_gpu, sizeof(double)*xDim*yDim);

        for(int i=0; i<xDim; ++i){
                for(int j=0; j<yDim; ++j){
                        v1[i*yDim + j] = 1.0;
                }
        }
        cudaMemcpy(v1_gpu, v1, sizeof(double)*xDim*yDim, cudaMemcpyHostToDevice);
        scalVecMult_dd<<<256,256>>>(v1_gpu, 2.0, v1_gpu);       
        cudaMemcpy(v1, v1_gpu, sizeof(double)*xDim*yDim, cudaMemcpyDeviceToHost);
        printf("%e\n",v1[0]);
        vecVecMult_dd<<<256,256>>>(v1_gpu, v1_gpu, v1_gpu);       
        cudaMemcpy(v1, v1_gpu, sizeof(double)*xDim*yDim, cudaMemcpyDeviceToHost);
        printf("%e\n",v1[0]);
	free(v1);cudaFree(v1_gpu);

	//#######################################################################

        double2 *v2, *v2_gpu;
        v2 = (double2*) malloc(sizeof(double2)*xDim*yDim);
        cudaMalloc((void**) &v2_gpu, sizeof(double2)*xDim*yDim);

        for(int i=0; i<xDim; ++i){
                for(int j=0; j<yDim; ++j){
                        v2[i*yDim + j].x = 1.0;
                        v2[i*yDim + j].y = 1.0;
                }
        }
        cudaMemcpy(v2_gpu, v2, sizeof(double2)*xDim*yDim, cudaMemcpyHostToDevice);
        scalVecMult_d2d<<<256,256>>>(v2_gpu, 2.0, v2_gpu);       
        cudaMemcpy(v2, v2_gpu, sizeof(double2)*xDim*yDim, cudaMemcpyDeviceToHost);
        printf("Re=%e	Im=%e\n",v2[0].x,v2[0].y);
        vecVecMult_d2d2<<<256,256>>>(v2_gpu, v2_gpu, v2_gpu);       
        cudaMemcpy(v2, v2_gpu, sizeof(double2)*xDim*yDim, cudaMemcpyDeviceToHost);
        printf("Re=%e	Im=%e\n",v2[0].x,v2[0].y);
}

int main(){
	test_scalVectMult();
	return 0;
}
