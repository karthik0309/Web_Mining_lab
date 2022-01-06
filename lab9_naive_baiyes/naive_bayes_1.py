from csv import reader
import termtables as tt

class NaiveBayesClassifier(object):
    def __init__(self,dataset_filename):
        csvfile = open(dataset_filename, 'r')
        self.dataset_ = list(reader(csvfile))
        self.training_dataset=[]
        self.testing_dataset=[]
        self.vocabulary_set=set()
        self.prior_probability={}
        self.dict_by_class={'India':{},'Bangladesh':{},'Others':{}}


        self.seperate_datasets()
        self.get_vocabulary()
        self.get_prior_probability()
        self.get_word_probability()

    def seperate_datasets(self):
        training_flag=-1
        print('\nRecords of the dataset')
        for row in self.dataset_:
            if row[0]=="training data":
                training_flag=1
            if row[0]=="test data":
                training_flag=0
            
            if training_flag==-1:
                continue

            if training_flag==1:
                self.training_dataset.append([row[1],row[2]])
            else:
                self.testing_dataset.append(row[1])
        
            print(row)
        print("Training data")
        for row in self.training_dataset:
            print(row)
        print("Testing data")
        for row in self.testing_dataset:
            print(row)
        print('')

    def get_vocabulary(self):
        for data in self.training_dataset:
            seperated_data=data[0].split("-")
            for word in seperated_data:
                self.vocabulary_set.add(word)
                if word in self.dict_by_class[data[1]]:
                    self.dict_by_class[data[1]][word]+=1
                else:
                    self.dict_by_class[data[1]][word]=1
            
        for data in self.testing_dataset:
            seperated_data=data[0].split("-")
            for word in seperated_data:
                self.vocabulary_set.add(word)
        
        for key,value in self.dict_by_class.items():
            print(key)
            print(value)
            print('')
        print("Len of vocabulary set is: "+str(len(self.vocabulary_set)))

    def get_prior_probability(self):
        unique_class={}
        no_of_docs=0
        for data in self.training_dataset:
            if data[1] in unique_class:
                unique_class[data[1]]=unique_class[data[1]]+1
            else:
                unique_class[data[1]]=1
            no_of_docs+=1
        for key,val in unique_class.items():
            self.prior_probability[key]=val/no_of_docs
        
        print("Initial prior probability")
        print(self.prior_probability)
        return
    
    def get_word_probability(self):
        for _,classList in self.dict_by_class.items():
            for word,freq in classList.items():
                classList[word]=round((freq+1)/(len(classList)+len(self.vocabulary_set)),6)

    def predict_testclass(self):
        print("The record belongs to class")
        finalResult=[]
        for record in self.testing_dataset:
            seperated_word = record.split("-")
            max_probability=-10
            record_belongs_to_class=''
            for uniqueClass,classList in self.dict_by_class.items():
                probability=self.prior_probability[uniqueClass]
                sum=0
                for word in seperated_word:
                    if word in classList:
                        sum+=classList[word]
                probability=sum
                if probability==self.prior_probability[uniqueClass]:
                    probability=0.00000

                if probability>max_probability:
                    max_probability=probability
                    record_belongs_to_class=uniqueClass
            finalResult.append([record,record_belongs_to_class])
        string = tt.to_string(
                finalResult,
                header=["Document", "class"],
                style=tt.styles.ascii_thin_double,
                # alignment="ll",
                # padding=(0, 1),
                )
        print(string)            


dataset_file = input('Enter the name of the dataset file:\t')
nvc = NaiveBayesClassifier(dataset_file)
nvc.predict_testclass()