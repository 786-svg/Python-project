import pandas as pd
df1 = pd.read_excel('Input_1.xlsx')
df2 = pd.read_excel('Input_2.xlsx')
df1.drop(['S No'],axis=1,inplace=True)
df2.drop(['S No'],axis=1,inplace=True)
df3 = pd.merge(df1,df2,left_on='User ID',right_on='uid',how='left')
df3.drop(['uid','name'],axis=1,inplace=True)
df4=pd.DataFrame(df3.groupby(['Team Name'])['total_statements','total_reasons'].mean())
df4['Rank']= df4[['total_statements','total_reasons']].apply(tuple,axis=1).rank(method='dense',ascending=False).astype(int)
nms=['Rank','Team Name','total_statements','total_reasons']
df4.reindex(columns=nms)
df4=df4[df4.columns[[2,0,1]]]
df4.rename(columns = {'total_statements':'Average Statements','total_reasons':'Average Reasons'}, inplace = True)
df6=pd.DataFrame()
df5=pd.DataFrame(df3.groupby(['Team Name']))
df6['Thinking Team LeaderBoard']=df5[0]
df4.index=[0,1,2,3,4,5,6,7,8]
df4=pd.merge(df6, df4, left_index=True, right_index=True)
df4=df4[df4.columns[[1,0,2,3]]]
df4=pd.DataFrame(df4)
df4=pd.DataFrame(df4.sort_values(by=['Rank']))
df4.to_excel('output.xlsx')
