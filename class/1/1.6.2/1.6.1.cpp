
// Copyright 2019 © Ramon Romero @RamonRomeroQro
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.
// Special thanks to: 
// @Manchas2k4, @alelopezperez and the FLOSS comunity.

#include <iostream>
using namespace std;

int main(){
int w,x,y,z;
int i =4; int j = 5;
{
    int j= 7;
    i = 6;
    w = i+j;
}
x = i+j;
{
    int i=8;
    y=i+j;
}
z=i+j;
cout << "w:" << w << " y:" << y << " x:" <<x << " z:"<<z << endl;
return 0;
}
