# https://help.blackboard.com/Learn/Instructor/Tests_Pools_Surveys/Reuse_Questions/Upload_Questions


def render_mc(question_dict):
    text = 'MC\t'
    text += question_dict['question'] + '\t'
    choices = question_dict['choices']
    correct = question_dict['correct']
    # The correct answer can be provided using a index integer
    if isinstance(correct, int):
        new_correct = [0] * len(choices)
        new_correct[correct] = 1
        correct = new_correct

    for ch, cr in zip(choices, correct):
        if cr:  cr_text = 'correct'
        if not cr: cr_text = 'incorrect'
        text += str(ch) + '\t' + str(cr_text) + '\t'
    text.rstrip('\t')
    return text


def render_tf(question_dict):
    text = 'TF\t'
    text += question_dict['question'] + '\t'
    answer = question_dict['answer']
    if answer: text += 'true'
    if not answer: text += 'false'
    return text


def render_es(question_dict):
    text = 'ESS\t'
    text += question_dict['question'] + '\t'
    if 'example' in question_dict: text += question_dict['example'] + '\t'
    text.rstrip('\t')
    return text


def print_message(message, variant='msg'):
    print(variant, message)


class Test:
    def __init__(self):
        self.questions = []
        self.definitions = {'mc': ['question', 'choices', 'correct'], \
                            'es': ['question'], \
                            'tf': ['question', 'answer']}

    def check_question_arguments(self, question_type, arguments):
        required = set(self.definitions[question_type])
        provided = set(arguments.keys())
        provided.remove('type')
        missing = required.difference(provided)
        missing = list(missing)
        return missing

    def add_questions(self, **kwargs):
        missing = self.check_question_arguments(kwargs['type'], kwargs)
        if len(missing) == 0:
            self.questions.append(kwargs)
            print_message('Added ' + kwargs['type'] + ' question', 'msg')
        else:
            print_message('Missing arguments ' + str(missing) + ' for question type ' + kwargs['type'], 'wrn')

    def render_questions(self, file_name=False):
        all_questions = ''
        for question in self.questions:
            question_type = question['type']
            if question_type == 'mc': render = render_mc(question)
            if question_type == 'tf': render = render_tf(question)
            if question_type == 'es': render = render_es(question)
            all_questions = all_questions + render + '\n'
        all_questions = all_questions.rstrip('\n')
        if file_name:
            f = open(file_name, 'w')
            f.write(all_questions)
            f.close()
        return all_questions


a = Test()

a.add_questions(type='mc', question='test')
a.add_questions(type='mc', question='Which of the following is a vowel?', choices=['a', 'b', 'c'], correct=0)
a.add_questions(type='tf', question='Do pigs fly?', answer=False)
a.add_questions(type='tf', question='Do birds fly?', answer=True)
a.add_questions(type='es', question='Do birds fly?', example='Yes, birds have feathers, therefore...')

a.render_questions('test.txt')
