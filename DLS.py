import pandas as pd
dl=pd.read_csv('DLS.csv')
df=pd.DataFrame(dl)
run1=int(input('How many runs did Team 1 get ?\n'))
wk1=int(input('How many Wickets has the team 1 lost?\n'))
print(f'Runs :{run1}')
for i in range(1):
    if wk1!=10:
        ovr1=int(input('How many overs team 1 played\n'))
        if ovr1>20:
            rov1=50-ovr1
            st=str(wk1)
            res=(df.loc[ovr1,st]) 
            fstres=(100-(res))
        else:
            print('According to ICC rules, a minimum of 20 overs must be played to use the DLS method in an ODI match.')
            break
    else:
        fstres=100
        ovr1=int(input('How many overs team 1 played\n'))
    print(f'Run rate:{run1/ovr1:.2f}')

    snd=int(input('Enter 1 if the second innings has stared , or enter 2 if it has not\n'))
    if snd==1:
        run2=int(input('How many runs did Team 2 get ?\n'))
        wk2=int(input('How many Wickets has the team 2 lost?\n'))
        povr=int(input('How many overs team 2 played\n'))
        ovr2=int(input('For how many overs are they restricting the 2nd innings?\n'))
        rov2=50-ovr2
        res2=(df.loc[rov2,'0'])
        #print(res2)
        Target= int(run1*(res2/fstres))
        print(f'Target :{Target}')
        print(f'Required Run rate :{Target/ovr2:.2f}')
    elif snd==2:
        ovr2=int(input('How many overs can be played in 2nd innings ?\n'))
        rov2=50-ovr2
        res2=(df.loc[rov2,'0'])
        #print(res2)
        Target= int(run1*(res2/fstres))
        print(f'Target :{Target}')
        print(f'Required Run rate :{Target/ovr2:.2f}')