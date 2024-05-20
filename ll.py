models = []
    models.append(('Gradient Boosting', GradientBoostingClassifier()))
    models.append(('Light Gradient Boosting', LGBMClassifier()))
    models.append(('Random Forest', RandomForestClassifier()))
    models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))
    models.append(('Logistic Regression', LogisticRegression()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('Extra Trees', ExtraTreesClassifier()))
    models.append(('SVM', SVC()))
    models.append(('AdaBoost', AdaBoostClassifier()))
    models.append(('Ridge', RidgeClassifier()))
    models.append(('Dummy', DummyClassifier()))
    models.append(('Decision Tree', DecisionTreeClassifier()))
    models.append(('Naive Bayes', GaussianNB()))
    models.append(('Quadratic Discriminant Analysis', QuadraticDiscriminantAnalysis()))
    
    results = []
    names = []
    scoring = 'accuracy'
    
    for name, model in models:
        kfold = KFold(n_splits=10, random_state=42, shuffle=True)
        cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        
    plt.figure(figsize=(10,7))
    plt.boxplot(results, labels=names)
    plt.title('Algorithm Comparison')

    # swap the axes
    plt.xlabel('Algorithm')
    plt.ylabel('Accuracy')
    plt.xticks(rotation=90)

    plt.show()