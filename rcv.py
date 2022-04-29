def get_file_contents(filename):
    '''
    This function takes in a argument called  filename then calls that function and reads the file and puts the values in a string called
    "results" and then returns the results
    '''
    results = ""
    try:
        file = open(filename,'r')
        lines = file.readlines()
        for line in lines:
            one_line = line.split('\n')
            results = results + "\n" + one_line[0]
        return results
    except:
        return None
def get_votes(string):
    '''
    This function takes in a string argument called 'string; and turns it into a list while
    splitting at any instance at "\n"and adding those values to a list called "results"
    Then returns results
    '''
    results = []
    list = string.split('\n')
    for index in list:
        if len(index) > 0:
            results.append(index.split(','))
    return results
def borda_scores(votes):
    '''
    This function takes in a list of lists argument called 'votes' and gives creates a dictionary called 'results'
    and adds values to the keys based on the number of times a candidate was voted for and how early in the list
    they appeared.
    and return the dictionary 'results'
    '''
    results = {}
    point = 0
    for vote in votes:
        point = len(vote)
        for index in vote:
            if index not in results:
                results[index] = 0
            results[index] = results[index] + point
            point = point - 1
    return results
def plurality(votes):
    '''
    This function takes in a list of lists argument called 'votes'
    and sees how many times the first value in the list is the first value among all of the lists.
    It records these results in a dictionary called 'results'
    then it returns 'results'
    '''
    results = {}
    for vote in votes:
        if vote[0] not in results:
            results[vote[0]] = 0
        results[vote[0]] = results[vote[0]] + 1
    return results
def pairwise(votes):
    '''
    This function takes in a list of lists argument called 'votes' and compares each time a
    candidate was voted for over another candidate it records these results in a dictionary called 'results'
    then this function returns the dictionary 'results'
    '''
    results = {}
    pair = ()
    for vote in votes:
        for index in range(len(vote)-1):
            for endex in range(len(vote)-1):
                if index <= endex:
                    pair = (vote[index], vote[endex+1])
                    if pair not in results:
                        results[pair] = 0
                    results[pair] = results[pair] + 1
    return results
def condorcet_winner(votes):
    '''
    This function takes in a list of lists argument called 'votes' and sees how many times each candidate beat the other candidates.
    the candidate that beat the other candidates the most is the winner.
    This function records the winner in a string variable called 'result'
    This function then returns 'result'
    '''
    result_string = ""
    result = []
    results = []
    parings = pairwise(votes)
    points = {}
    largest = 0
    for key in parings:
        pair2 = key[1],key[0]
        for key2 in parings:
            if len(parings) < 2:
                results.append(key)
            if key2 == pair2:
                if parings[key] > parings[key2]:
                    results.append(key)
    for index in range(len(results)):
        winner = results[index]
        if winner[0] not in points:
            points[winner[0]] = 0
        points[winner[0]] = points[winner[0]] + 1
    for key in points:
        if points[key] > largest:
            largest = points[key]
            result.append(key)
        if points[key] == largest and result[0] != key:
            result.append(key)
    if len(result) > 1:
        return None
    result_string = result[0]
    return result_string
def winners(scores):
    '''
    this function takes in a dictionary argument called 'scores' and sees which key has the highest value.
    then puts this key in a list called "results" if multiple values have the same highest value
     it adds them all to the list.
     then returns the list called "results"
    '''
    results = []
    largest = 0
    for key in scores:
        if scores[key] > largest:
            largest = scores[key]
            results = []
            results.append(key)
        elif scores[key] == largest:
            results.append(key)
    return results
