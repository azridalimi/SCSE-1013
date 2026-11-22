#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cctype>
using namespace std;
int gx = 10;
void showLocal(){ int gx = 3; cout << gx; }
void byVal(int x){ x = x + 10; }
void byRef(int &x){ x = x + 10; }
int sq(int n){ return n*n; }
int add(int a, int b = 5){ return a + b; }
double avg(int a, int b){ return (a + b) / 2; }
void counter(){ static int c = 0; c++; cout << c << " "; }
void swapV(int a, int b){ int t=a; a=b; b=t; }
void swapR(int &a, int &b){ int t=a; a=b; b=t; }
int twice(int n){ return n*2; }
double twice(double n){ return n*2.5; }
int main(){
  cout << "T3a: "; { int a=7,b=2; cout << a / b << " " << a % b; } cout << "\n";
  cout << "T3b: "; { int y=-5; int z = 8 - 3 + 9 / 2 + 2 * -y; cout << z << " "; z = 8 - (3 + 9 / 2) + 2 * -y; cout << z; } cout << "\n";
  cout << "T3c: "; { int count=5, first=10, second; second = 5*count-- + first; cout << second << " " << count << " "; second = 5*--count + first; cout << second << " " << count; } cout << "\n";
  cout << "T3d: " << 7 / 2 * 2.0 << " " << 2.0 * 7 / 2 << "\n";
  cout << "T3e: "; { int sum=241; cout << sum / 3 << " " << static_cast<double>(sum) / 3; } cout << "\n";
  cout << "T3f: "; { char c='C'; cout << int(c) << " " << char(c+1); } cout << "\n";
  cout << "T3g: " << 075 << " " << 0x75A << " " << 1234L << "\n";
  cout << "T3h: "; { unsigned char u=255; u++; cout << (int)u << " "; unsigned char z=0; z--; cout << (int)z << " "; short s=32767; s++; cout << s; } cout << "\n";
  cout << "T3i: "; { int a=1; double d=1.0; d += 1.5*3 + (++a); cout << d << " " << a << " "; a=1; d=1.0; d -= 1.5*3 + a++; cout << d << " " << a; } cout << "\n";
  cout << "T3j: "; { int i=10,j=2; i *= j + 3; cout << i; } cout << "\n";
  cout << "T3k: " << 46 / 9 << " " << 46 % 9 + 4 * 4 - 2 << " " << 45 + 43 % 5 * (23 * 3 % 2) << " " << 13 % 5 << "\n";
  cout << "T3l: "; { int a=1; a %= 3 / a + 3; cout << a; } cout << "\n";
  cout << "T3m: "; { int x,p,q; x = p = q = 5; cout << x+p+q; } cout << "\n";
  cout << "T3n: "; { int s=3725; cout << s/3600 << " h " << (s%3600)/60 << " min " << s%60 << " s"; } cout << "\n";
  cout << "T3o: " << 0.25*(4250.50*11 - 3*450) << " " << 0.25*(4000*11 - 2*450) << "\n";
  cout << "T3p: "; { int x=5; cout << x++ << " "; cout << x << " "; cout << ++x; } cout << "\n";
  cout << "T3q: " << 10 / 4 << " " << 10.0 / 4 << " " << 10 % 4 << " " << (double)(10/4) << "\n";
  cout << "T3r: "; { int r=10; const double PI=3.14159; cout << 2*r << " " << 2*PI*r << " " << PI*r*r; } cout << "\n";
  cout << "T4a: "; { int tickets=5; if ((tickets = 0)) cout << "Sold out"; else cout << "Left " << tickets; } cout << "\n";
  cout << "T4b: "; { int x=2; switch(x){ case 1: cout<<"A"; case 2: cout<<"B"; case 3: cout<<"C"; break; default: cout<<"D"; } } cout << "\n";
  cout << "T4c: "; for(int i=10;i>0;i-=2) cout << i << " "; cout << "\n";
  cout << "T4d: "; { int n=10; do { cout << n; n++; } while (n<5); } cout << "\n";
  cout << "T4e: "; { int i; for(i=0;i<3;i++); cout << i; } cout << "\n";
  cout << "T4g: "; { int inner=0; for(int i=1;i<=3;i++){ for(int j=1;j<=i;j++){ cout<<"*"; inner++; } cout<<"/"; } cout << " inner=" << inner; } cout << "\n";
  cout << "T4h: "; for(int i=1;i<=6;i++){ if(i==3) continue; if(i==5) break; cout << i << " "; } cout << "\n";
  cout << "T4i: " << -3 % 2 << " " << 7 % -2 << "\n";
  cout << "T4k: "; { int i=1,total=0; while(i<=5){ total+=i; i++; } cout << total; } cout << "\n";
  cout << "T4l: "; { int a=4,b=9; cout << (a>b ? a : b); } cout << "\n";
  cout << "T4m: "; { int a=5,b=2; if(a>3) { if(b>3) cout<<"X"; else cout<<"Y"; } } cout << "\n";
  cout << "T4n: "; { int c=0; for(int i=0;i<5;i++) c++; cout << c << " "; c=0; for(int i=0;i<=5;i++) c++; cout << c; } cout << "\n";
  cout << "T4o: "; for (int y : {1900, 2000, 2024, 2100}) cout << ((y%4==0 && y%100!=0) || y%400==0) << " "; cout << "\n";
  cout << "T4p: "; { int score=90; char g; if(score>90) g='A'; else if(score>75) g='B'; else if(score>60) g='C'; else if(score>50) g='D'; else g='F'; cout << g; } cout << "\n";
  cout << "T4q: "; { int n=3; while(n>0){ cout << n << "... "; n--; } cout << "Go!"; } cout << "\n";
  cout << "T4r: "; { int i=0; while(i<5){ i++; if(i%2==0) continue; cout << i << " "; } } cout << "\n";
  cout << "T4s: "; { int x=7; if(x>5 && x<10) cout << "in"; else cout << "out"; cout << " " << !(x>5) << " " << (x==7 || x/0); } cout << "\n";
  cout << "T4t: "; { char op='+'; int a=6,b=3; switch(op){ case '+': cout<<a+b; break; case '-': cout<<a-b; break; default: cout<<"?"; } } cout << "\n";
  cout << "T4u: "; { int sum=0,n; int data[]={12,-5,0,20,7,4,-1}; int k=0,cnt=0; while(true){ n=data[k++]; if(n==-1) break; if(n<1) continue; sum+=n; cnt++; } cout << cnt << " " << sum << " " << (double)sum/cnt; } cout << "\n";
  cout << "T4v: "; for(int i=1;i<=3;i++){ for(int j=1;j<=2;j++) cout << i*j << " "; } cout << "\n";
  cout << "T5a: " << strcmp("abc","abc") << " " << (strcmp("abc","abd")<0) << "\n";
  cout << "T5b: " << atoi("12abc") << " " << atoi("abc") << " " << atof("3.9") << " " << atoi("3.9") << " " << atoi("-8") << "\n";
  cout << "T5c: " << pow(2,3) << " " << sqrt(16) << " " << ceil(2.1) << " " << floor(-2.5) << " " << fabs(-3.5) << " " << floor(2.9) << "\n";
  cout << "T5d: " << toupper('a') << " " << char(toupper('a')) << " " << (char)tolower('Q') << "\n";
  cout << "T5f: "; { int a=5; byVal(a); cout << a << " "; byRef(a); cout << a; } cout << "\n";
  cout << "T5i: "; showLocal(); cout << " " << gx << "\n";
  cout << "T5j: "; counter(); counter(); counter(); cout << "\n";
  cout << "T5k: " << sq(3) + sq(2) << "\n";
  cout << "T5l: " << add(2) << " " << add(2,3) << "\n";
  cout << "T5m: " << twice(4) << " " << twice(4.0) << "\n";
  cout << "T5n: " << strlen("Hello") << "\n";
  cout << "T5o: " << sqrt(pow(4-1,2)+pow(6-2,2)) << " " << acos(-1.0)*3*3 << "\n";
  cout << "T5s: " << avg(3,4) << "\n";
  cout << "T5h: "; { int a=1,b=2; swapV(a,b); cout << a << b << " "; swapR(a,b); cout << a << b; } cout << "\n";
  cout << "T5t: "; { char s[20]; strcpy(s,"Hi"); strcat(s," there"); cout << s << " " << strlen(s); } cout << "\n";
  cout << "T5u: " << (isdigit('7')!=0) << " " << (isalpha('7')!=0) << " " << (isupper('a')!=0) << " " << (ispunct('!')!=0) << "\n";
  cout << "T5v: " << abs(-7) << " " << pow(9,0.5) << " " << sqrt(2) << "\n";
  return 0;
}
