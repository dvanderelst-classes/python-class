import expyriment

test = False


if test: expyriment.control.set_develop_mode()

# Define response buttons

key_negative = expyriment.misc.constants.K_a
key_positive = expyriment.misc.constants.K_l

# Read stimuli

f = open('stimuli.txt', 'r')
stimuli = f.readlines()
f.close()

# Build block and trials

exp = expyriment.design.Experiment(name="E-detection")
block1 = expyriment.design.Block(name="block_1")
if test: stimuli = stimuli[0:3]
for line in stimuli:
    line = line.rstrip('\r')
    line = line.rstrip('\n')
    line = line.split(' ')
    word = line[0]
    condition = line[1]
    valence = line[2]
    trial = expyriment.design.Trial()
    trial.set_factor('condition', condition)
    trial.set_factor('valence', valence)
    trial.set_factor('word', word)
    stim = expyriment.stimuli.TextLine(text=word)
    trial.add_stimulus(stim)
    block1.add_trial(trial)
    print(word, trial.factor_dict)

block1.shuffle_trials()
exp.add_block(block1)

exp.data_variable_names = ['name', "trial", 'word', 'condition', 'valence', "btn", "rt", 'correct']

# Start experimental control

expyriment.control.initialize(exp)
expyriment.control.start()

# Get pp name

input_field = expyriment.io.TextInput('name')
name = input_field.get()

# Instructions

screen_ready = expyriment.stimuli.TextScreen('Start', 'Press the spacebar to start the experiment')
screen_ready.present()
exp.keyboard.wait()

# Make feedback screens and fix cross

fix_cross = expyriment.stimuli.FixCross()
feedback_correct = expyriment.stimuli.BlankScreen(colour=(0, 250,0))
feedback_error = expyriment.stimuli.BlankScreen(colour=(250, 0,0))

for block in exp.blocks:
    for trial in block.trials:
        fix_cross.present()
        exp.clock.wait(500)
        trial.stimuli[0].present()
        key, rt = exp.keyboard.wait([key_negative, key_positive])
        condition = trial.get_factor('condition')
        valence = trial.get_factor('valence')
        word = trial.get_factor('word')

        correct = False
        if valence == 'positive' and key == key_positive: correct = True
        if valence == 'negative' and key == key_negative: correct = True

        if correct: feedback_correct.present()
        if not correct: feedback_error.present()
        exp.clock.wait(500)

        exp.data.add([name, trial.id, word, condition, valence, key, rt, correct])

expyriment.control.end()
exp.data.save()
