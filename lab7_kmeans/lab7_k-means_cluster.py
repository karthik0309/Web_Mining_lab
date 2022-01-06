import string
import numpy as np
import os 
import math

class document_clustering(object):

    def __init__(self, file_dict, word_list, k):
        self.file_dict = file_dict
        self.word_list = word_list
        self.k = k

    def tokenize_document(self, document):

        terms = document.lower().split()
        return [term.strip(string.punctuation) for term in terms]

    def create_word_listing(self):

        self.listing_dict_ = {}
        dir = os.path.dirname(__file__)
        for id in self.file_dict:
            temp_word_list = []
            filename=os.path.join(dir, self.file_dict[id])
            f = open(filename, 'r')
            document = f.read()
            terms = self.tokenize_document(document)
            for term in self.word_list:
                temp_word_list.append(terms.count(term.lower()))
            self.listing_dict_[id] = temp_word_list

        print('Word listing of each document')
        for id in self.listing_dict_:
            print('%d\t%s' % (id, self.listing_dict_[id]))

    def find_centroid(self, feature):

        distances = []
        for centroid in self.centroids_:
            dist = 0
            for i in range(0,len(self.centroids_[centroid])):
                dist += pow((self.centroids_[centroid][i] - feature[i]),2)
            dist = math.sqrt(dist)
            distances.append(round(dist,2))
        return distances
        # return np.argmin(distances)

    def kmeans_clustering(self):

        centroid = [1,3,5,4]
        self.centroids_ = {}
        for i in range(self.k):
            self.centroids_[i] = self.listing_dict_[centroid[i]]

        for i in range(2):
            self.classes_ = {}
            self.features_ = {}

            for i in range(self.k):
                self.classes_[i] = []
                self.features_[i] = [self.centroids_[i]]
            
            print("Distance between all points and centroids: ")
            for id in self.listing_dict_:
                distances = self.find_centroid(self.listing_dict_[id])
                print(distances)
                classification =  np.argmin(distances)
                self.classes_[classification].append(id)
                self.features_[classification].append(self.listing_dict_[id])

            previous = dict(self.centroids_)

            # Recalculate the cluster centroid based on the documents alloted
            for i in self.features_:
                self.centroids_[i] = np.average(self.features_[i], axis = 0)

            isOptimal = True

            for centroid in self.centroids_:
                original_centroid = np.array(previous[centroid])
                curr_centroid = self.centroids_[centroid]

                if np.sum(original_centroid - curr_centroid) != 0:
                    isOptimal = False

            # Breaking the results if the centroids found are optimal
            if isOptimal:
                break

    def print_clusters(self):
        print('\nFinal Clusters')
        for i in self.classes_:
            print('%d:-->%s' % (i+1, self.classes_[i]))




file_dict = {1: 'documents/doc1.txt',
             2: 'documents/doc2.txt',
             3: 'documents/doc3.txt',
             4: 'documents/doc4.txt',
             5: 'documents/doc5.txt'}

word_list = ['Fighter','India', 'France', 'UK']


document_cluster = document_clustering(file_dict = file_dict, word_list = word_list, k = 4)
document_cluster.create_word_listing()
document_cluster.kmeans_clustering()
document_cluster.print_clusters()