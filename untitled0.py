#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 21:29:47 2019

@author: marufshaikh
"""
fo=open("code.txt","r")
str1=fo.read()
print(str1)
list=[]
#sym={}
ps=["START","USING","DC","DS","END"]
op={"L":4,"A":4,"ST":4}
ad={}
list=str1.split('\n')
#print(list)
#c=0
for i in range(0,len(list[0])):
    #print(list[0][i:i+5])
    if list[0][i:i+5]=="START":
       # st=int(list[0][i+7::])
       st=int(list[0][i+6::])
       #print(st)
       break
for i in list:
    ch=""
    for j in i:
        if j!=" ":
            ch=ch+j
        else:
            break
    #print(ch)
    ad[ch]=st
    if ch in op:
        st=st+op[ch]
    if ps.count(ch)==0 and ch not in op:
        #print(ch)
        nw=""
        for j in i:
            if j!=" ":
                nw=nw+j
            elif nw==ch:
                nw=""
            else:
                if nw=='END':
                    break
                if nw=="DC" or nw=="DS":
                    if i[len(ch)+len(nw)+2]=='F' or i[len(ch)+len(nw)+3]=='F':
                        st=st+4
                    elif i[len(ch)+len(nw)+2]=='A' or i[len(ch)+len(nw)+3]=='A':
                        st=st+2
    
    if ch=="END":
        break
print(ad)
symb={}
for i in ad:
    #print(i)
    if ps.count(i)==0 and i not in op:
        #print(i)
        symb[i]=ad[i]
        
print("Symbol Tabe:\nSymbol\t\t\tAddress")
for i in symb:       
    print(i,"\t\t\t",symb[i])
    
    
lt={} 
hex={'L':'58','A':'5A','ST':'50'}
print("Second Pass:") 
#Experiment 4
for i in list:
    ch=""
    for j in i:
        if j!=" ":
            ch=ch+j
        else:
            if ch in op:
                x=i.split(' ')
                a,b=i.split(',')
                #print(x,b,symb[b])
                #z=symb[b]
                #print(ad[x[0]])
                print(ad[x[0]]," ",hex[x[0]]," 1,",symb[b],"(0,15)")
#print(lt)
#print(str(5))

                