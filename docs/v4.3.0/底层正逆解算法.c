#define PI 3.14159265
#define rad 0.01745329


void Matrix_mul(float InMatrix1[4][4], float InMatrix2[4][4], float OuMatrix[4][4]) {
    OuMatrix[0][0] = InMatrix1[0][0]*InMatrix2[0][0] + InMatrix1[0][1]*InMatrix2[1][0] + InMatrix1[0][2]*InMatrix2[2][0] + InMatrix1[0][3]*InMatrix2[3][0];
    OuMatrix[0][1] = InMatrix1[0][0]*InMatrix2[0][1] + InMatrix1[0][1]*InMatrix2[1][1] + InMatrix1[0][2]*InMatrix2[2][1] + InMatrix1[0][3]*InMatrix2[3][1];
    OuMatrix[0][2] = InMatrix1[0][0]*InMatrix2[0][2] + InMatrix1[0][1]*InMatrix2[1][2] + InMatrix1[0][2]*InMatrix2[2][2] + InMatrix1[0][3]*InMatrix2[3][2];
    OuMatrix[0][3] = InMatrix1[0][0]*InMatrix2[0][3] + InMatrix1[0][1]*InMatrix2[1][3] + InMatrix1[0][2]*InMatrix2[2][3] + InMatrix1[0][3]*InMatrix2[3][3];
    OuMatrix[1][0] = InMatrix1[1][0]*InMatrix2[0][0] + InMatrix1[1][1]*InMatrix2[1][0] + InMatrix1[1][2]*InMatrix2[2][0] + InMatrix1[1][3]*InMatrix2[3][0];
    OuMatrix[1][1] = InMatrix1[1][0]*InMatrix2[0][1] + InMatrix1[1][1]*InMatrix2[1][1] + InMatrix1[1][2]*InMatrix2[2][1] + InMatrix1[1][3]*InMatrix2[3][1];
    OuMatrix[1][2] = InMatrix1[1][0]*InMatrix2[0][2] + InMatrix1[1][1]*InMatrix2[1][2] + InMatrix1[1][2]*InMatrix2[2][2] + InMatrix1[1][3]*InMatrix2[3][2];
    OuMatrix[1][3] = InMatrix1[1][0]*InMatrix2[0][3] + InMatrix1[1][1]*InMatrix2[1][3] + InMatrix1[1][2]*InMatrix2[2][3] + InMatrix1[1][3]*InMatrix2[3][3];
    OuMatrix[2][0] = InMatrix1[2][0]*InMatrix2[0][0] + InMatrix1[2][1]*InMatrix2[1][0] + InMatrix1[2][2]*InMatrix2[2][0] + InMatrix1[2][3]*InMatrix2[3][0];
    OuMatrix[2][1] = InMatrix1[2][0]*InMatrix2[0][1] + InMatrix1[2][1]*InMatrix2[1][1] + InMatrix1[2][2]*InMatrix2[2][1] + InMatrix1[2][3]*InMatrix2[3][1];
    OuMatrix[2][2] = InMatrix1[2][0]*InMatrix2[0][2] + InMatrix1[2][1]*InMatrix2[1][2] + InMatrix1[2][2]*InMatrix2[2][2] + InMatrix1[2][3]*InMatrix2[3][2];
    OuMatrix[2][3] = InMatrix1[2][0]*InMatrix2[0][3] + InMatrix1[2][1]*InMatrix2[1][3] + InMatrix1[2][2]*InMatrix2[2][3] + InMatrix1[2][3]*InMatrix2[3][3];
    OuMatrix[3][0] = InMatrix1[3][0]*InMatrix2[0][0] + InMatrix1[3][1]*InMatrix2[1][0] + InMatrix1[3][2]*InMatrix2[2][0] + InMatrix1[3][3]*InMatrix2[3][0];
    OuMatrix[3][1] = InMatrix1[3][0]*InMatrix2[0][1] + InMatrix1[3][1]*InMatrix2[1][1] + InMatrix1[3][2]*InMatrix2[2][1] + InMatrix1[3][3]*InMatrix2[3][1];
    OuMatrix[3][2] = InMatrix1[3][0]*InMatrix2[0][2] + InMatrix1[3][1]*InMatrix2[1][2] + InMatrix1[3][2]*InMatrix2[2][2] + InMatrix1[3][3]*InMatrix2[3][2];
    OuMatrix[3][3] = InMatrix1[3][0]*InMatrix2[0][3] + InMatrix1[3][1]*InMatrix2[1][3] + InMatrix1[3][2]*InMatrix2[2][3] + InMatrix1[3][3]*InMatrix2[3][3];
}

void Matrix_inv(float InMatrix[4][4],float OuMatrix[4][4]){      
     float a = InMatrix[0][0]*InMatrix[1][1]*InMatrix[2][2]*InMatrix[3][3] - InMatrix[0][0]*InMatrix[1][1]*InMatrix[2][3]*InMatrix[3][2] - InMatrix[0][0]*InMatrix[1][2]*InMatrix[2][1]*InMatrix[3][3] + InMatrix[0][0]*InMatrix[1][2]*InMatrix[2][3]*InMatrix[3][1] + InMatrix[0][0]*InMatrix[1][3]*InMatrix[2][1]*InMatrix[3][2] - InMatrix[0][0]*InMatrix[1][3]*InMatrix[2][2]*InMatrix[3][1] - InMatrix[0][1]*InMatrix[1][0]*InMatrix[2][2]*InMatrix[3][3] + InMatrix[0][1]*InMatrix[1][0]*InMatrix[2][3]*InMatrix[3][2] + InMatrix[0][1]*InMatrix[1][2]*InMatrix[2][0]*InMatrix[3][3] - InMatrix[0][1]*InMatrix[1][2]*InMatrix[2][3]*InMatrix[3][0] - InMatrix[0][1]*InMatrix[1][3]*InMatrix[2][0]*InMatrix[3][2] + InMatrix[0][1]*InMatrix[1][3]*InMatrix[2][2]*InMatrix[3][0] + InMatrix[0][2]*InMatrix[1][0]*InMatrix[2][1]*InMatrix[3][3] - InMatrix[0][2]*InMatrix[1][0]*InMatrix[2][3]*InMatrix[3][1] - InMatrix[0][2]*InMatrix[1][1]*InMatrix[2][0]*InMatrix[3][3] + InMatrix[0][2]*InMatrix[1][1]*InMatrix[2][3]*InMatrix[3][0] + InMatrix[0][2]*InMatrix[1][3]*InMatrix[2][0]*InMatrix[3][1] - InMatrix[0][2]*InMatrix[1][3]*InMatrix[2][1]*InMatrix[3][0] - InMatrix[0][3]*InMatrix[1][0]*InMatrix[2][1]*InMatrix[3][2] + InMatrix[0][3]*InMatrix[1][0]*InMatrix[2][2]*InMatrix[3][1] + InMatrix[0][3]*InMatrix[1][1]*InMatrix[2][0]*InMatrix[3][2] - InMatrix[0][3]*InMatrix[1][1]*InMatrix[2][2]*InMatrix[3][0] - InMatrix[0][3]*InMatrix[1][2]*InMatrix[2][0]*InMatrix[3][1] + InMatrix[0][3]*InMatrix[1][2]*InMatrix[2][1]*InMatrix[3][0];
     OuMatrix[0][0] = (InMatrix[1][1]*InMatrix[2][2]*InMatrix[3][3] - InMatrix[1][1]*InMatrix[2][3]*InMatrix[3][2] - InMatrix[1][2]*InMatrix[2][1]*InMatrix[3][3] + InMatrix[1][2]*InMatrix[2][3]*InMatrix[3][1] + InMatrix[1][3]*InMatrix[2][1]*InMatrix[3][2] - InMatrix[1][3]*InMatrix[2][2]*InMatrix[3][1])/a;
     OuMatrix[0][1] = -(InMatrix[0][1]*InMatrix[2][2]*InMatrix[3][3] - InMatrix[0][1]*InMatrix[2][3]*InMatrix[3][2] - InMatrix[0][2]*InMatrix[2][1]*InMatrix[3][3] + InMatrix[0][2]*InMatrix[2][3]*InMatrix[3][1] + InMatrix[0][3]*InMatrix[2][1]*InMatrix[3][2] - InMatrix[0][3]*InMatrix[2][2]*InMatrix[3][1])/a;
     OuMatrix[0][2] = (InMatrix[0][1]*InMatrix[1][2]*InMatrix[3][3] - InMatrix[0][1]*InMatrix[1][3]*InMatrix[3][2] - InMatrix[0][2]*InMatrix[1][1]*InMatrix[3][3] + InMatrix[0][2]*InMatrix[1][3]*InMatrix[3][1] + InMatrix[0][3]*InMatrix[1][1]*InMatrix[3][2] - InMatrix[0][3]*InMatrix[1][2]*InMatrix[3][1])/a;   
     OuMatrix[0][3] = -(InMatrix[0][1]*InMatrix[1][2]*InMatrix[2][3] - InMatrix[0][1]*InMatrix[1][3]*InMatrix[2][2] - InMatrix[0][2]*InMatrix[1][1]*InMatrix[2][3] + InMatrix[0][2]*InMatrix[1][3]*InMatrix[2][1] + InMatrix[0][3]*InMatrix[1][1]*InMatrix[2][2] - InMatrix[0][3]*InMatrix[1][2]*InMatrix[2][1])/a;
     OuMatrix[1][0] = -(InMatrix[1][0]*InMatrix[2][2]*InMatrix[3][3] - InMatrix[1][0]*InMatrix[2][3]*InMatrix[3][2] - InMatrix[1][2]*InMatrix[2][0]*InMatrix[3][3] + InMatrix[1][2]*InMatrix[2][3]*InMatrix[3][0] + InMatrix[1][3]*InMatrix[2][0]*InMatrix[3][2] - InMatrix[1][3]*InMatrix[2][2]*InMatrix[3][0])/a;
     OuMatrix[1][1] = (InMatrix[0][0]*InMatrix[2][2]*InMatrix[3][3] - InMatrix[0][0]*InMatrix[2][3]*InMatrix[3][2] - InMatrix[0][2]*InMatrix[2][0]*InMatrix[3][3] + InMatrix[0][2]*InMatrix[2][3]*InMatrix[3][0] + InMatrix[0][3]*InMatrix[2][0]*InMatrix[3][2] - InMatrix[0][3]*InMatrix[2][2]*InMatrix[3][0])/a;
     OuMatrix[1][2] = -(InMatrix[0][0]*InMatrix[1][2]*InMatrix[3][3] - InMatrix[0][0]*InMatrix[1][3]*InMatrix[3][2] - InMatrix[0][2]*InMatrix[1][0]*InMatrix[3][3] + InMatrix[0][2]*InMatrix[1][3]*InMatrix[3][0] + InMatrix[0][3]*InMatrix[1][0]*InMatrix[3][2] - InMatrix[0][3]*InMatrix[1][2]*InMatrix[3][0])/a;   
     OuMatrix[1][3] = (InMatrix[0][0]*InMatrix[1][2]*InMatrix[2][3] - InMatrix[0][0]*InMatrix[1][3]*InMatrix[2][2] - InMatrix[0][2]*InMatrix[1][0]*InMatrix[2][3] + InMatrix[0][2]*InMatrix[1][3]*InMatrix[2][0] + InMatrix[0][3]*InMatrix[1][0]*InMatrix[2][2] - InMatrix[0][3]*InMatrix[1][2]*InMatrix[2][0])/a;
     OuMatrix[2][0] = (InMatrix[1][0]*InMatrix[2][1]*InMatrix[3][3] - InMatrix[1][0]*InMatrix[2][3]*InMatrix[3][1] - InMatrix[1][1]*InMatrix[2][0]*InMatrix[3][3] + InMatrix[1][1]*InMatrix[2][3]*InMatrix[3][0] + InMatrix[1][3]*InMatrix[2][0]*InMatrix[3][1] - InMatrix[1][3]*InMatrix[2][1]*InMatrix[3][0])/a;
     OuMatrix[2][1] = -(InMatrix[0][0]*InMatrix[2][1]*InMatrix[3][3] - InMatrix[0][0]*InMatrix[2][3]*InMatrix[3][1] - InMatrix[0][1]*InMatrix[2][0]*InMatrix[3][3] + InMatrix[0][1]*InMatrix[2][3]*InMatrix[3][0] + InMatrix[0][3]*InMatrix[2][0]*InMatrix[3][1] - InMatrix[0][3]*InMatrix[2][1]*InMatrix[3][0])/a;
     OuMatrix[2][2] = (InMatrix[0][0]*InMatrix[1][1]*InMatrix[3][3] - InMatrix[0][0]*InMatrix[1][3]*InMatrix[3][1] - InMatrix[0][1]*InMatrix[1][0]*InMatrix[3][3] + InMatrix[0][1]*InMatrix[1][3]*InMatrix[3][0] + InMatrix[0][3]*InMatrix[1][0]*InMatrix[3][1] - InMatrix[0][3]*InMatrix[1][1]*InMatrix[3][0])/a;   
     OuMatrix[2][3] = -(InMatrix[0][0]*InMatrix[1][1]*InMatrix[2][3] - InMatrix[0][0]*InMatrix[1][3]*InMatrix[2][1] - InMatrix[0][1]*InMatrix[1][0]*InMatrix[2][3] + InMatrix[0][1]*InMatrix[1][3]*InMatrix[2][0] + InMatrix[0][3]*InMatrix[1][0]*InMatrix[2][1] - InMatrix[0][3]*InMatrix[1][1]*InMatrix[2][0])/a;
     OuMatrix[3][0] = -(InMatrix[1][0]*InMatrix[2][1]*InMatrix[3][2] - InMatrix[1][0]*InMatrix[2][2]*InMatrix[3][1] - InMatrix[1][1]*InMatrix[2][0]*InMatrix[3][2] + InMatrix[1][1]*InMatrix[2][2]*InMatrix[3][0] + InMatrix[1][2]*InMatrix[2][0]*InMatrix[3][1] - InMatrix[1][2]*InMatrix[2][1]*InMatrix[3][0])/a;
     OuMatrix[3][1] = (InMatrix[0][0]*InMatrix[2][1]*InMatrix[3][2] - InMatrix[0][0]*InMatrix[2][2]*InMatrix[3][1] - InMatrix[0][1]*InMatrix[2][0]*InMatrix[3][2] + InMatrix[0][1]*InMatrix[2][2]*InMatrix[3][0] + InMatrix[0][2]*InMatrix[2][0]*InMatrix[3][1] - InMatrix[0][2]*InMatrix[2][1]*InMatrix[3][0])/a;
     OuMatrix[3][2] = -(InMatrix[0][0]*InMatrix[1][1]*InMatrix[3][2] - InMatrix[0][0]*InMatrix[1][2]*InMatrix[3][1] - InMatrix[0][1]*InMatrix[1][0]*InMatrix[3][2] + InMatrix[0][1]*InMatrix[1][2]*InMatrix[3][0] + InMatrix[0][2]*InMatrix[1][0]*InMatrix[3][1] - InMatrix[0][2]*InMatrix[1][1]*InMatrix[3][0])/a;
     OuMatrix[3][3] = (InMatrix[0][0]*InMatrix[1][1]*InMatrix[2][2] - InMatrix[0][0]*InMatrix[1][2]*InMatrix[2][1] - InMatrix[0][1]*InMatrix[1][0]*InMatrix[2][2] + InMatrix[0][1]*InMatrix[1][2]*InMatrix[2][0] + InMatrix[0][2]*InMatrix[1][0]*InMatrix[2][1] - InMatrix[0][2]*InMatrix[1][1]*InMatrix[2][0])/a;
 }


// j 六轴关节角度
// pa 返回的末端工具坐标与姿态
void FK(float j[6], float pa[6]){
     float a1[4][4] = {
    { cos(j[0]), 0.0, -sin(j[0]), cos(j[0])*24.0 },
    { sin(j[0]), 0.0, cos(j[0]), sin(j[0])*24.0 },
    { 0.0, -1.0, 0.0, 153.5 },
    { 0.0, 0.0, 0.0, 1.0 },
                       };
     float a2[4][4] = {
    { sin(j[1]), cos(j[1]), 0.0, sin(j[1])*160.72 },
    { -cos(j[1]), sin(j[1]), 0.0, -cos(j[1])*160.72 },
    { 0.0, 0.0, 1.0, 0.0 },
    { 0.0, 0.0, 0.0, 1.0 },
                       };     
     float a3[4][4] = {
    { cos(j[2]), 0.0, -sin(j[2]), 0.0 },
    { sin(j[2]), 0.0, cos(j[2]), 0.0 },
    { 0.0, -1.0, 0.0, 0.0 },
    { 0.0, 0.0, 0.0, 1.0 },
                       };
     float a4[4][4] = {
    { cos(j[3]), 0.0, sin(j[3]), 0.0 },
    { sin(j[3]), 0.0, -cos(j[3]), 0.0 },
    { 0.0, 1.0, 0.0, 220.5 },
    { 0.0, 0.0, 0.0, 1.0 },
                       };   
     float a5[4][4] = {
    { -sin(j[4]), 0.0, -cos(j[4]), 0.0 },
    { cos(j[4]), 0.0, -sin(j[4]), 0.0 },
    { 0.0, -1.0, 0.0, 0.0 },
    { 0.0, 0.0, 0.0, 1.0 },
                       };                          
     float a6[4][4] = {
    { cos(j[5]), -sin(j[5]), 0.0, 0.0 },
    { sin(j[5]), cos(j[5]), 0.0, 0.0 },
    { 0.0, 0.0, 1.0, 79.29 },
    { 0.0, 0.0, 0.0, 1.0 },
                       }; 
    float arr1[4][4] = {{0.0}} ;
    float arr2[4][4] = {{0.0}} ;
    float arr3[4][4] = {{0.0}} ;
    float arr4[4][4] = {{0.0}} ;
    float at[4][4] = {{0.0}};
    Matrix_mul(a1, a2, arr1);
    Matrix_mul(arr1, a3, arr2);
    Matrix_mul(arr2, a4, arr3);
    Matrix_mul(arr3, a5, arr4);
    Matrix_mul(arr4, a6, at);
    pa[0]=at[0][3];
    pa[1]=at[1][3];
    pa[2]=at[2][3];
    float rx;
    float ry;
    float rz;
    ry = atan2(-at[2][0],sqrt(at[0][0]*at[0][0] + at[1][0]*at[1][0]));
    if (fabs(ry - PI*0.5) <= 0.0001)
     {
        ry = PI*0.5;
        rz = 0.0;
        rx = atan2(at[1][1],at[0][1]);
     }
     else
     {
        if (fabs(ry + PI*0.5) <= 0.0001)
        {
           ry = -PI*0.5;
           rz = 0.0;
           rx = atan2(-at[1][1],at[0][1]);
        }
        else
        {
           rx = atan2(at[2][1]/cos(ry),at[2][2]/cos(ry));
           rz = atan2(at[1][0]/cos(ry),at[0][0]/cos(ry));
        }
     }
    pa[3] = rx;
    pa[4] = ry;
    pa[5] = rz;
}
// fb x,y,z,Rx,Ry,Rz
// inj 当前的关节角度
// ouj 逆解的关节角度
void IK(float fb[6], float inj[6],float ouj[6]){
     float T_Matrix[4][4];
     T_Matrix[0][0] = cos(fb[5])*cos(fb[4]);
     T_Matrix[0][1] = cos(fb[5])*sin(fb[4])*sin(fb[3])-sin(fb[5])*cos(fb[3]);
     T_Matrix[0][2] = cos(fb[5])*sin(fb[4])*cos(fb[3])+sin(fb[5])*sin(fb[3]);
     T_Matrix[0][3] = fb[0];
     T_Matrix[1][0] = sin(fb[5])*cos(fb[4]);
     T_Matrix[1][1] = sin(fb[5])*sin(fb[4])*sin(fb[3])+cos(fb[5])*cos(fb[3]);
     T_Matrix[1][2] = sin(fb[5])*sin(fb[4])*cos(fb[3])-cos(fb[5])*sin(fb[3]);
     T_Matrix[1][3] = fb[1];
     T_Matrix[2][0] = -sin(fb[4]);
     T_Matrix[2][1] = cos(fb[4])*sin(fb[3]);
     T_Matrix[2][2] = cos(fb[4])*cos(fb[3]);
     T_Matrix[2][3] = fb[2];
     T_Matrix[3][0] = 0.0;
     T_Matrix[3][1] = 0.0;
     T_Matrix[3][2] = 0.0;
     T_Matrix[3][3] = 1.0;

     float px = T_Matrix[0][3]-79.29*T_Matrix[0][2];
     float py = T_Matrix[1][3]-79.29*T_Matrix[1][2];
     float pz = T_Matrix[2][3]-79.29*T_Matrix[2][2];

     float j1 = 0.0;
     float j1_1 = atan2(py,px);
     float j1_2 = atan2(-py,-px);

     if(fabs(j1_1 - inj[0]) <= fabs(j1_2 - inj[0]))
     {
        j1 = j1_1;
     }
     else
     {
        j1 = j1_2;
     }
     
     float temp1 = sqrt( (px-24.0*cos(j1)) * (px-24.0*cos(j1)) + (py-24.0*sin(j1)) * (py-24.0*sin(j1)) + (pz-153.5) * (pz-153.5) );
     float j3 = 0.0;
     float j3_1 = PI*0.5-acos((74451.1684-temp1*temp1)/70877.52);
     float j3_2 = -(PI*1.5-acos((74451.1684-temp1*temp1)/70877.52));
     if(fabs(j3_1 - inj[2]) <= fabs(j3_2 - inj[2]))
     {
        j3 = j3_1;
     }
     else
     {
        j3 = j3_2;
     }
      
     float temp2 = atan2(-220.5*cos(j3),160.72-220.5*sin(j3));
     float temp3 = atan2(sqrt((160.72 - 220.5*sin(j3)) * (160.72 - 220.5*sin(j3)) + 48620.25 * cos(j3) * cos(j3) - (pz-153.5)*(pz-153.5)), pz-153.5);
     float j2 = 0.0;
     float j2_1 = temp2 + temp3;
     float j2_2 = temp2 - temp3;
     if(fabs(j2_1 - inj[1]) <= fabs(j2_2 - inj[1]))
     {
        j2 = j2_1;
     }
     else
     {
        j2 = j2_2;
     }   

    float a1[4][4] = {
    { cos(j1), 0.0, -sin(j1), cos(j1)*24.0 },
    { sin(j1), 0.0, cos(j1), sin(j1)*24.0 },
    { 0.0, -1.0, 0.0, 153.5 },
    { 0.0, 0.0, 0.0, 1.0 },
                       };
    float a2[4][4] = {
    { sin(j2), cos(j2), 0.0, sin(j2)*160.72 },
    { -cos(j2), sin(j2), 0.0, -cos(j2)*160.72 },
    { 0.0, 0.0, 1.0, 0.0 },
    { 0.0, 0.0, 0.0, 1.0 },
                       }; 
    float a3[4][4] = {
    { cos(j3), 0.0, -sin(j3), 0.0 },
    { sin(j3), 0.0, cos(j3), 0.0 },
    { 0.0, -1.0, 0.0, 0.0 },
    { 0.0, 0.0, 0.0, 1.0 },
                       };
    float arr1[4][4] = {{0}};
    float arr2[4][4] = {{0}};
    float arr3[4][4] = {{0}};
    float t36[4][4] = {{0}};
    Matrix_mul(a1,a2,arr1);
    Matrix_mul(arr1,a3,arr2);
    Matrix_inv(arr2,arr3);
    Matrix_mul(arr3,T_Matrix,t36);
    float temp4 = atan2(sqrt(1.0-t36[2][2]*t36[2][2]),-t36[2][2]);
    float j5 = 0.0;
    float j4 = 0.0;
    float j6 = 0.0;
    float j5_1 = PI*0.5-temp4;
    float j5_2 = -(PI*1.5-temp4);
    if(fabs(j5_1 - inj[4]) <= fabs(j5_2 - inj[4]))
    {
      j5 = j5_1;
      j4 = atan2(-t36[1][2],-t36[0][2]);
      j6 = atan2(-t36[2][1],t36[2][0]);
    }
    else
    {
      j5 = j5_2;
      j4 = atan2(t36[1][2],t36[0][2]);
      j6 = atan2(t36[2][1],-t36[2][0]);
    } 
    ouj[0] = j1;
    ouj[1] = j2;
    ouj[2] = j3;
    ouj[3] = j4;
    ouj[4] = j5;
    ouj[5] = j6;
    
}