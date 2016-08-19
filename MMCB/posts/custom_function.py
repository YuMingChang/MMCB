def req_field_get(request, fieldName):      # Get by id of html
    tmp_list = []
    for i in range(10):
        ctx = request.POST.get(fieldName + str(i), 'None')
        if ctx != '' and ctx != 'None':
            tmp_list.append(ctx)

    while '' in tmp_list:
        tmp_list.remove('')

    return tmp_list

def req_field_getlist(request, fieldName):      # Get by name of html
    tmp_list = request.POST.getlist(fieldName)
    print (tmp_list)
    while '' in tmp_list:
        tmp_list.remove('')
    print (tmp_list)
    return tmp_list
    # How to send multiple input field values with same name?
    # http://stackoverflow.com/questions/478382/how-to-send-multiple-input-field-values-with-same-name

# request.POST.get('sth') vs request.POST['sth'] - difference?
# http://stackoverflow.com/questions/12518517/request-post-getsth-vs-request-poststh-difference
