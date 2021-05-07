## README

### Essential Features of a Synthetic Dataset for Machine Learning (ML)

It is understood, at this point, that a synthetic dataset is generated programmatically, and not sourced from any kind of social or scientific experiment, business transactional data, sensor reading, or manual labeling of images. However, such datasets are definitely not completely random, and the generation and usage of synthetic data for ML must be guided by some overarching needs. In particular,

- It can be numeric, binary, or categorical (ordinal or non-ordinal) and the number of features and length of the dataset could be arbitrary.
- There must be some degree of randomness to it but, at the same time, the user should be able to choose a wide variety of statistical distribution to base this data upon, i.e., the underlying random process can be precisely controlled and tuned.
- If it is used for classification algorithms, then the degree of class separation should be controllable to make the learning problem easy or hard.
- Random noise can be interjected in a controllable manner.
- Speed of generation should be quite high to enable experimentation with a large variety of such datasets for any particular ML algorithms, i.e., if the synthetic data is based on data augmentation on a real-life dataset, then the augmentation algorithm must be computationally efficient.
- For a regression problem, a complex, non-linear generative process can be used for sourcing the data – real physics models may come to aid in this endeavor.

### Existing solutions


|Project name|Domain|Programming language|Github|tutorial|
|----|----|----|----|----|
|Synthea Patient Generator|Medical|Java|https://github.com/synthetichealth/synthea|https://github.com/synthetichealth/synthea/wiki| 
|DataSynthesizer|Medical|Python-3|https://github.com/theodi/synthetic-data-tutorial/tree/master/DataSynthesizer|https://github.com/theodi/synthetic-data-tutorial/blob/master/README.md|
|DataSynthesizer|General|Python-3|https://github.com/DataResponsibly/DataSynthesizer|https://github.com/DataResponsibly/DataSynthesizer/blob/master/docs/cr-datasynthesizer-privacy.pdf|
|Faker|General|Python|https://github.com/joke2k/faker|https://faker.readthedocs.io/en/master/|


