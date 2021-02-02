from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from . forms import predictonForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from . models import Prediction1
from . models import FinalTrainDf
from . serializer import predictionSerializers
import pickle
import joblib as jb
import numpy as np
from sklearn import preprocessing
import pandas as pd
from collections import defaultdict, Counter
from django.db.models import Q
from django.db.models import Sum
import math

# Create your views here.
class predictionView(viewsets.ModelViewSet):

    queryset = Prediction1.objects.all()
    serializer_class = predictionSerializers

    # def list(self, request):
    #     return JsonResponse({'status': 'ok'})

    def create(self, request):
        print("*************")
        marka= request.data['marka']
        model= request.data['model']
        year= request.data['year']
        engine= request.data['engine']
        gearbox= request.data['gearbox']
        transmission=request.data['transmission']
        ban_type = request.data['ban_type']
        fuel_type = request.data['fuel_type']
        color =request.data['color']
        used_by_km = request.data['used_by_km']
    


        myDict = (request.data)
        

        df=pd.DataFrame(myDict, index=[0])
        #df1 = df[['year',  'engine' ,   'gearbox' ,   'transmission' , 'ban_type' , 'fuel_type',  'color' ,  'used_by_km']].copy()
        #print(df1)

        query1=FinalTrainDf.objects.filter(marka=marka,model=model,year=year, engine=engine , gearbox=gearbox,transmission=transmission,
        ban_type=ban_type,fuel_type=fuel_type,color=color)

        if len(query1) < 4:
            p = Prediction1(marka=marka,model=model,year=year, engine=engine , gearbox=gearbox,transmission=transmission,
            ban_type=ban_type,fuel_type=fuel_type,color=color,used_by_km=used_by_km,predicted_price=0
            )
            p.save()
            return Response( 'Our experts will call you')
           # return JsonResponse({'Message': 'Our experts will call you'}, safe=False)
        else:


            df2=ml_predict( df)
            #print(df2)
            result = pd.concat([df, df2], axis=1, sort=False)
            #print(result)
            p = Prediction1(marka=marka,model=model,year=year, engine=engine , gearbox=gearbox,transmission=transmission,
            ban_type=ban_type,fuel_type=fuel_type,color=color,used_by_km=used_by_km,predicted_price=result['predicted_price']
            )
            p.save()
            



        
            #return JsonResponse( result['predicted_price'], safe=False)
            return Response(result['predicted_price'])


    





def ml_predict(unit):
    unit1 = unit[['year',  'engine' ,   'gearbox' ,   'transmission' , 'ban_type' , 'fuel_type',  'color' ,  'used_by_km']].copy()
    try:
        print(unit['marka'].values[0] , unit['model'].values[0] )

        if (unit['marka'].values[0]==1) and (unit['model'].values[0]==38): 
            print('hi')
            mdl=jb.load("decision_tree_hyundai_accent.pkl")

        if (unit['marka'].values[0]==1) and (unit['model'].values[0]==29): 
            mdl=jb.load("decision_tree_hyundai_elantra.pkl")

        if (unit['marka'].values[0]==9) and (unit['model'].values[0]==11): 
            print('hi')
            mdl=jb.load("decision_tree_chevrolet_cruze2.pkl")

        y_pred=mdl.predict(unit1)
        newdf=pd.DataFrame(y_pred , columns=['predicted_price'])
        return newdf
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)



def cxcontact(request):

    if request.method=='POST':
        forms=predictonForm(request.POST)
        if forms.is_valid():
            marka = forms.cleaned_data['marka']
            model = forms.cleaned_data['model']
            year =  forms.cleaned_data['year']
            engine= forms.cleaned_data['engine']
            gearbox= forms.cleaned_data['gearbox']
            transmission=forms.cleaned_data['transmission']
            ban_type = forms.cleaned_data['ban_type']
            fuel_type = forms.cleaned_data['fuel_type']
            color = forms.cleaned_data['color']
            used_by_km = forms.cleaned_data['used_by_km']


            myDict = (request.POST).dict()
            df=pd.DataFrame(myDict, index=[0])
            print(df)
            # df1 = df[['year',  'engine' ,   'gearbox' ,   'transmission' , 'ban_type' , 'fuel_type',  'color' ,  'used_by_km']].copy()

            query1=FinalTrainDf.objects.filter(marka=marka,model=model,year=year, engine=engine , gearbox=gearbox,transmission=transmission,
            ban_type=ban_type,fuel_type=fuel_type,color=color)

            if len(query1) < 4:
                #print('Our experts will call you')
                messages.success(request,'Our experts will call you')
                #return JsonResponse({'Message': 'Our experts will call you'}, safe=False)
                p = Prediction1(marka=marka,model=model,year=year, engine=engine , gearbox=gearbox,transmission=transmission,
                ban_type=ban_type,fuel_type=fuel_type,color=color,used_by_km=used_by_km,predicted_price=0
                )
                p.save()

            else:


                df2=ml_predict( df)
                result = pd.concat([df, df2], axis=1, sort=False)
                #print(result)
    




            
                p = Prediction1(marka=marka,model=model,year=year, engine=engine , gearbox=gearbox,transmission=transmission,
                ban_type=ban_type,fuel_type=fuel_type,color=color,used_by_km=used_by_km,predicted_price=result['predicted_price']
                )
                p.save()


                messages.success(request,'predicted price: {0} '.format(result['predicted_price'].values[0]))
            
        
    forms=predictonForm()
        
    return render(request, 'myform/cxform.html', {'forms':forms})


