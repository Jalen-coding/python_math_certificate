def add_time(start, duration,day=False):
  days_of_week_dict={'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
  days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  d_t=duration.partition(':')
  d_hour=int(d_t[0])
  d_min=int(d_t[2])
  
  split=start.partition(':')
  split2=split[2].partition(' ')
  s_hour=int(split[0])
  s_min=int(split2[0])
  ampm=split2[2]
  am_and_pm={'AM':'PM','PM':'AM'}

  amount_of_days=int(d_hour/24) 
#sum minutes
  sum_min=s_min+d_min
  if(sum_min>=60):
    s_hour+=1
    sum_min=sum_min % 60
    sum_hour=(s_hour+d_hour) % 12

  amount_ampm_flip=int((s_hour+d_hour)/12)
  sum_hour=(s_hour+d_hour) % 12

#sum hours
  sum_min=sum_min if sum_min > 9 else '0' + str(sum_min)
  sum_hour=sum_hour=12 if sum_hour==0 else sum_hour
  if (ampm=='PM' and s_hour +(d_hour % 12) >=12):
    amount_of_days+=1
  
  ampm =am_and_pm[ampm]if amount_ampm_flip % 2==1 else ampm
  time=str(sum_hour)+':'+str(sum_min)+' '+ampm

  if (day):
    day = day.capitalize()
    index=int((days_of_week_dict[day])+amount_of_days) % 7
    new_day=days[index]
    time +=', '+new_day

  if(amount_of_days==1):
    return time + '' + ' (next day)'
  
  elif (amount_of_days>1):
    return time + ' ('+str(amount_of_days)+' days later)'
  
  return time
