# graduate-admission
Predicting the chances of admit in graduate program of universities in USA. Dataset from UCI machine learning repository.

## Overview
The following document will specify how to use the API to predict the chance of admit. The predicted chance of admit is sent back in JSON.

|     **Data Object**    |  **Constraints**   |
|------------------------|--------------------|
| GRE                    |   160 - 340        |
| TOEFL                  |   100 - 120        |
| CGPA                   |   0 - 8            |
| University Rating      |   0 - 5            |
| SOP                    |   0 - 5            |

Here, University rating with 1 is considered highest and SOP with rating 5 is considered highest.


## Methods
There is only 1 method by which the chance of admit can be predicted
### All

|     **Data Object**    |  **Constraints**   |
|------------------------|--------------------|
| GRE                    |        310         |
| TOEFL                  |        120         |
| CGPA                   |        10          |
| University Rating      |        3           |
| SOP                    |        5           |

- [https://predictadmit.herokuapp.com/predict?gre=310&toefl=120&cgpa=10&unirating=3&sop=5](https://predictadmit.herokuapp.com/predict?gre=310&toefl=120&cgpa=10&unirating=3&sop=5)
<br><br>Result:
``` 
    {
      "acceptance": 0.9353784949486199
    }
```

This will predict the data with the parameters sent and will return the chance of admit in percentage in JSON.
