from course import corgis

import graduates
data = graduates.get_majors()
data = corgis.data2frame(data)
data = data.query('Salaries_Quantity>0')
data.to_csv('graduates.csv',index=False)
