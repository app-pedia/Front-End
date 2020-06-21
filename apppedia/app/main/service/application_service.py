from app.main import db
from app.main.model.application import Application
from app.main.model.function import Function

def application_save(data):
    application = Application.query.filter_by(public_id=data['public_id']).first()
    if not application:
        new_application = Application(
            public_id = data['public_id'],
            name = data['name'],
            category = data['category'],
            developer_name = data['developer_name'],
            developer_public_id = data['developer_public_id'],
            rating_total = data['rating_total'],
            rating_average = data['rating_average'],
            rating_five = data['rating_five'],
            rating_four = data['rating_four'],
            rating_three = data['rating_three'],
            rating_two = data['rating_two'],
            rating_one = data['rating_one'],
            install = data['install'],
            install_link = data['install_link'],
            image_logo = data['image_logo'],
            price = data['price'],
            update_date = data['update_date'],
            size = data['size'],
            version_current = data['version_current'],
            version_needs = data['version_needs'],
            contents_grade = data['contents_grade'],
            interaction = data['interaction'],
            in_app_products = data['in_app_products'],
            related_name = data['related_name'],
            related_link = data['related_link']
        )
        save_changes(new_application)
        response_object = {
            'status': 'success',
            'message': 'Successfully saved.',
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Application already exists.',
        }
        return response_object, 409

def application_auto():
    auto = {'name': []}
    word = []
    application = Application.query.all()
    for i in application:
        word.append(i.name)
    auto['name'] = word
    return auto

def application_srch(data):
    result_list = []
    result_real = []
    ''' Application Search about Name '''
    application = Application.query.filter_by(name=data['word']).first()
    if application:
        result_temp = {'public_id': 'null', 'score': 0.0}
        art = int(application.rating_total)
        ara = float(application.rating_average)
        ai = int(application.install)
        ap = 0
        if application.price != 'Free':
            apt = str(application.price)[1:]
            ap = float(apt)
        avn = 0.0
        if application.version_needs != '기기에 따라 다릅니다.':
            avt = str(application.version_needs)[0:2]
            avn = float(avt)
        if ((data['category'] == application.category or data['category'] == 'string') or
            (data['developer_name'] == application.developer_name or data['developer_name'] == 'string') or
            (int(data['rating_lower_total']) <= art and art <= int(data['rating_upper_total'])) or
            (float(data['rating_lower_average']) <= ara and ara <= float(data['rating_upper_average'])) or
            (int(data['install_lower']) <= ai and ai <= int(data['install_upper'])) or
            (float(data['price_lower']) <= ap and ap <= float(data['price_upper']))):
            (avn == 0.0 or avn <= float(data['version_needs']))):
            score_all = ara + ((float(len(application.rating_total)) + float(application.rating_total[0]) * 0.1) + (float(len(application.install)) + float(application.install[0]) * 0.1)) * 0.5
            score_fnt = 0.0
            function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_five']).first()
            if function:
                score_fnt += 10.0
            function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_four']).first()
            if function:
                score_fnt += 8.0
            function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_three']).first()
            if function:
                score_fnt += 6.0
            function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_two']).first()
            if function:
                score_fnt += 4.0
            function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_one']).first()
            if function:
                score_fnt += 2.0
            score_all += score_fnt/3
            result_temp['public_id'] = application.public_id
            result_temp['score'] = score_all
            result_list.append(result_temp)
    ''' Application Search about Category '''
    application = Application.query.filter_by(category=data['word']).all()
    if application:
        for i in application:
            result_temp = {'public_id': 'null', 'score': 0.0}
            art = int(i.rating_total)
            ara = float(i.rating_average)
            ai = int(i.install)
            ap = 0
            if i.price != 'Free':
                apt = str(i.price)[1:]
                ap = float(apt)
            avn = 0.0
            if i.version_needs != '기기에 따라 다릅니다.':
                avt = str(i.version_needs)[0:2]
                avn = float(avt)
            if ((data['category'] == i.category or data['category'] == 'string') or
                (data['developer_name'] == i.developer_name or data['developer_name'] == 'string') or
                (int(data['rating_lower_total']) <= art and art <= int(data['rating_upper_total'])) or
                (float(data['rating_lower_average']) <= ara and ara <= float(data['rating_upper_average'])) or
                (int(data['install_lower']) <= ai and ai <= int(data['install_upper'])) or
                (float(data['price_lower']) <= ap and ap <= float(data['price_upper']))):
                (avn == 0.0 or avn <= float(data['version_needs']))):
                score_all = ara + ((float(len(i.rating_total)) + float(i.rating_total[0]) * 0.1) + (float(len(i.install)) + float(i.install[0]) * 0.1)) * 0.5
                score_fnt = 0.0
                function = Function.query.filter_by(application_public_id=i.public_id).filter_by(detail=data['function_five']).first()
                if function:
                    score_fnt += 10.0
                function = Function.query.filter_by(application_public_id=i.public_id).filter_by(detail=data['function_four']).first()
                if function:
                    score_fnt += 8.0
                function = Function.query.filter_by(application_public_id=i.public_id).filter_by(detail=data['function_three']).first()
                if function:
                    score_fnt += 6.0
                function = Function.query.filter_by(application_public_id=i.public_id).filter_by(detail=data['function_two']).first()
                if function:
                    score_fnt += 4.0
                function = Function.query.filter_by(application_public_id=i.public_id).filter_by(detail=data['function_one']).first()
                if function:
                    score_fnt += 2.0
                score_all += score_fnt/3
                result_temp['public_id'] = i.public_id
                result_temp['score'] = score_all
                result_list.append(result_temp)
    ''' Application Search about Developer '''
    application = Application.query.filter_by(developer_name=data['word']).all()
    if application:
        for i in application:
            result_temp = {'public_id': 'null', 'score': 0.0}
            art = int(i.rating_total)
            ara = float(i.rating_average)
            ai = int(i.install)
            ap = 0
            if i.price != 'Free':
                apt = str(i.price)[1:]
                ap = float(apt)
            avn = 0.0
            if i.version_needs != '기기에 따라 다릅니다.':
                avt = str(i.version_needs)[0:2]
                avn = float(avt)
            if ((data['category'] == i.category or data['category'] == 'string') or
                (data['developer_name'] == i.developer_name or data['developer_name'] == 'string') or
                (int(data['rating_lower_total']) <= art and art <= int(data['rating_upper_total'])) or
                (float(data['rating_lower_average']) <= ara and ara <= float(data['rating_upper_average'])) or
                (int(data['install_lower']) <= ai and ai <= int(data['install_upper'])) or
                (float(data['price_lower']) <= ap and ap <= float(data['price_upper']))):
                (avn == 0.0 or avn <= float(data['version_needs']))):
                score_all = ara + ((float(len(i.rating_total)) + float(i.rating_total[0]) * 0.1) + (float(len(i.install)) + float(i.install[0]) * 0.1)) * 0.5
                score_fnt = 0.0
                function = Function.query.filter_by(application_public_id=i.public_id).filter_by(detail=data['function_five']).first()
                if function:
                    score_fnt += 10.0
                function = Function.query.filter_by(application_public_id=i.public_id).filter_by(detail=data['function_four']).first()
                if function:
                    score_fnt += 8.0
                function = Function.query.filter_by(application_public_id=i.public_id).filter_by(detail=data['function_three']).first()
                if function:
                    score_fnt += 6.0
                function = Function.query.filter_by(application_public_id=i.public_id).filter_by(detail=data['function_two']).first()
                if function:
                    score_fnt += 4.0
                function = Function.query.filter_by(application_public_id=i.public_id).filter_by(detail=data['function_one']).first()
                if function:
                    score_fnt += 2.0
                score_all += score_fnt/3
                result_temp['public_id'] = i.public_id
                result_temp['score'] = score_all
                result_list.append(result_temp)
    ''' Application Search about Function '''
    function = Function.query.filter_by(detail=data['word']).all()
    if function:
        for i in function:
            result_temp = {'public_id': 'null', 'score': 0.0}
            application = Application.query.filter_by(public_id=i.application_public_id).first()
            art = int(application.rating_total)
            ara = float(application.rating_average)
            ai = int(application.install)
            ap = 0
            if application.price != 'Free':
                apt = str(application.price)[1:]
                ap = float(apt)
            avn = 0.0
            if application.version_needs != '기기에 따라 다릅니다.':
                avt = str(application.version_needs)[0:2]
                avn = float(avt)
            if ((data['category'] == application.category or data['category'] == 'string') or
                (data['developer_name'] == application.developer_name or data['developer_name'] == 'string') or
                (int(data['rating_lower_total']) <= art and art <= int(data['rating_upper_total'])) or
                (float(data['rating_lower_average']) <= ara and ara <= float(data['rating_upper_average'])) or
                (int(data['install_lower']) <= ai and ai <= int(data['install_upper'])) or
                (float(data['price_lower']) <= ap and ap <= float(data['price_upper']))):
                (avn == 0.0 or avn <= float(data['version_needs']))):
                score_all = ara + ((float(len(application.rating_total)) + float(application.rating_total[0]) * 0.1) + (float(len(application.install)) + float(application.install[0]) * 0.1)) * 0.5
                score_fnt = 0.0
                function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_five']).first()
                if function:
                    score_fnt += 10.0
                function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_four']).first()
                if function:
                    score_fnt += 8.0
                function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_three']).first()
                if function:
                    score_fnt += 6.0
                function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_two']).first()
                if function:
                    score_fnt += 4.0
                function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_one']).first()
                if function:
                    score_fnt += 2.0
                score_all += score_fnt/3
                result_temp['public_id'] = application.public_id
                result_temp['score'] = score_all
                result_list.append(result_temp)
    result_sort = sorted(result_list, key=(lambda x: x['score']))
    for i in result_sort:
        application = Application.query.filter_by(public_id=i['public_id']).first()
        result_real.append(application)
    result_real.reverse()
    return result_real

def application_comp(data):
    application = Application.query.filter_by(public_id=data['public_id']).first()
    result = {'public_id': 'null', 'name': 'null', 'category': 'null', 'image_logo': 'null', 'score_all': 0.0, 'score_rating_average': 0.0, 'score_rating_total': 0.0, 'score_install': 0.0, 'score_function_five': 0.0, 'score_function_four': 0.0, 'score_function_three': 0.0, 'score_function_two': 0.0, 'score_function_one': 0.0}
    if application:
        result['public_id'] = application.public_id
        result['name'] = application.name
        result['category'] = application.category
        result['image_logo'] = application.image_logo
        result['score_rating_average'] = float(application.rating_average)
        result['score_rating_total'] = float(len(application.rating_total)) + float(application.rating_total[0]) * 0.1
        result['score_install'] = float(len(application.install)) + float(application.install[0]) * 0.1
        function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_five']).first()
        if function:
            result['score_function_five'] = 10.0
        function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_four']).first()
        if function:
            result['score_function_four'] = 8.0
        function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_three']).first()
        if function:
            result['score_function_three'] = 6.0
        function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_two']).first()
        if function:
            result['score_function_two'] = 4.0
        function = Function.query.filter_by(application_public_id=application.public_id).filter_by(detail=data['function_one']).first()
        if function:
            result['score_function_one'] = 2.0
        result['score_all'] = round(result['score_rating_average'] + ((result['score_rating_total'] + result['score_install']) * 0.5) + (result['score_function_five'] + result['score_function_four'] + result['score_function_three'] + result['score_function_two'] + result['score_function_one'])/3, 2)
        result['score_rating_total'] = round(result['score_rating_total']/2, 2)
        result['score_install'] = round(result['score_install']/2, 2)
        result['score_function_five'] = round(result['score_function_five']/3, 2)
        result['score_function_four'] = round(result['score_function_four']/3, 2)
        result['score_function_three'] = round(result['score_function_three']/3, 2)
        result['score_function_two'] = round(result['score_function_two']/3, 2)
        result['score_function_one'] = round(result['score_function_one']/3, 2)
    return result

def application_info(public_id):
    return Application.query.filter_by(public_id=public_id).first()

def application_plus(category):
    plus = []
    application = Application.query.filter_by(category=category).all()
    for i in application:
        if (i.related_name != 'null') and (i.related_name != ''):
            plus.append(i)
    return plus

def save_changes(data):
    db.session.add(data)
    db.session.commit()