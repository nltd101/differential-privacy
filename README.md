
# Differential Privacy
- Using the Laplace mechanism
- Dataset [adult.csv](https://www.kaggle.com/wenruliu/adult-income-dataset)

## Definitions
*Note:`[Column Name]` refers to replacing it with the actual column name.*
### Pairwise Comparison

* ```([Column Name]:[Value])```

* **Example:** `(age:30)` means comparing `age` with `30`
### Comparison Operators
* ```{[Comparison Operator]:[Pairwise Comparison]}```

Symbol | Operators
------ | ----
`$gt` | >
`$lt` | <
`$eq` | =

*Note: Other operators can use the above comparison operators and the **not** operator below for inference.*
* **Example:** `{$gt:(age:30)}` is equivalent to `age>30`

### Logical Operators
* ```{[Logical Operators]:[[Sub-Operator],..]}```

Symbol | Operator | Number of Sub-Operators
------ | ---- |---
`$and` | and | 2
`$or` | or | 2
`$not` | not | 1


* **Example 1:**  ​`{$and:[{$gt:(age:30)},{$lt:(age:50)}]}` is equivalent to `age>30` **and** `age<50` 
* **Example 2:**  ​`{$not:[{$gt:(age:30)}]}` is equivalent to `age<=30` 

* **Example 3** ​

```base
{
​$or:[
​ {$gt:(age:30)},
​ {$and:[
​         {$lt:(age:20)},
​         {$not:[
             {$eq:(workclass:Private)}
               ]}
        ]
​    ]
}
```
Equivalent to:
```
(age>30) or (age<20 and not workclass==Private)
```

### Full Query
* `[Column].[Query Type]([Operator])`
* Example: `age.mean({$eq:(workclass:Private)})` returns the average `age` of records with `wordclass` as `Private`
*Note: If the Operator is left blank, the result will compute on the entire dataset.*
#### List of Query Types
* `min`: minimum value
* `max`: maximum value
* `mean`: mean
* `count`: count
* `median`: median
* `sum`: sum
* `variance`: variance
* `mode`: mode

*Note: For numeric queries, the column data must be numeric.*

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install the necessary packages.

```bash
pip install -r requirements.txt
```

## Sử dụng
Use [python](https://www.python.org/downloads/) to run the program.
```bash
python main.py
```

## Contribution
For change requests, please contact me and discuss the issue with me.
