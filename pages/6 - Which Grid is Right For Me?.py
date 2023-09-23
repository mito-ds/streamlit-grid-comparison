
import streamlit as st
    
st.markdown('### The Grid Quiz: Which Streamlit Grid is Right For Me?')

st.write("Check the boxes that apply to you, and then scroll down -- we'll tell you which grid is right for you and why!")

answers = {}

ALL_GRIDS = ['`st.table`', '`st.dataframe`', '`st.data_editor`', '`Mito`', '`AgGrid`']

DATA_SIZE_QUESTION = 'My dataset has:'

PERFORMANCE_QUESTIONS = [
    (
        DATA_SIZE_QUESTION,
        ['less than 50 rows', 'more than 50 rows', 'more than 2M rows'],
        [['st.table', '`st.dataframe`', '`st.data_editor`', '`Mito`', '`AgGrid`'], ['`st.dataframe`', '`st.data_editor`', '`Mito`', '`AgGrid`'], ['`Mito`']],
        ['is designed for small datasets', 'does not lay out all data statically, so it can handle large datasets', 'has ability to render > 200 MB of data by default']
    )
]

EXPLORATION_QUESTIONS = [
    (
        "I want built-in sorting",
        ['`st.dataframe`', '`st.data_editor`', '`Mito`', '`AgGrid`'],
        'has built-in sorting'
    ),
    (
        "I want built-in filtering",
        ['`Mito`', '`AgGrid`'],
        'has built-in filtering'
    ),
    (
        "I want built-in graphing",
        ['`Mito`'],
        'has built-in graphing'
    ), 
    (
        "I want to apply apply conditional formatting",
        ['`st.dataframe`', '`st.data_editor`', '`Mito`', '`AgGrid`'],
        'allows you to configure conditional formatting'
    ),
]

EDITING_QUESTIONS = [
    (
        "I want built-in single cell editing",
        ['`st.data_editor`', '`Mito`', '`AgGrid`'],
        'has built-in single cell editing'
    ),
    (
        "I want built-in Excel formulas",
        ['`Mito`'],
        'has built-in Excel formulas'
    ),
    (
        "I want built-in pivot tables",
        ['`Mito`'],
        'has built-in pivot tables'
    ),
    (
        "I want edits made to the grid to propagate to the rest of my app",
        ['`st.data_editor`', '`Mito`', '`AgGrid`'],
        'has built-in pivot tables'
    ),
    (
        "I want to record user edits and reuse them on other datasets",
        ['`Mito`'],
        'records user edits in a Python script that can be reused on other datasets'
    ),
]

CUSTOMIZATION_QUESTIONS = [
    (
        "I want to customize the grid's colors",
        ['`AgGrid`'],
        'allows you to customize the grid colors'
    ),
    (
        "I want to customize how cells are rendered",
        ['`AgGrid`'],
        'allows you to customize how cells are rendered using JavaScript'
    ),
]

RADIO_BUTTON_QUESTIONS = {
    'Performance Functionality': PERFORMANCE_QUESTIONS,
}

CHECKBOX_QUESTIONS = {
   
    'Exploration Functionality': EXPLORATION_QUESTIONS,
    'Editing Functionality': EDITING_QUESTIONS,
    'Grid Customization': CUSTOMIZATION_QUESTIONS,
}

for question_type, questions in RADIO_BUTTON_QUESTIONS.items():
    st.subheader(question_type)
    for question, options, grids_that_support_this, reason in questions:
        answer = st.radio(question, options=options)
        if answer:
            # Get the index of the answer from options
            answer_index = options.index(answer)
            answers[question] = (grids_that_support_this[answer_index], reason[answer_index])

for question_type, questions in CHECKBOX_QUESTIONS.items():
    st.subheader(question_type)
    for question, grids_that_support_this, reason in questions:
        answer = st.checkbox(question)
        if answer:
            answers[question] = (grids_that_support_this, reason)

st.subheader("Your Results")

if len(answers) == 1 and answers[DATA_SIZE_QUESTION][0][0] == 'st.table': 
    st.success("Since you're not looking for any functionality, we reccomend `st.table`! It's the simplest grid, and is great for displaying small datasets.")
else:
    
    available_grids = set(ALL_GRIDS)
    for grids, reason in answers.values():
        available_grids = available_grids.intersection(set(grids))

    if len(available_grids) == 0:
        # Show them the grids that support the most functionality, and tell them which features it doesn't support
        # Find the grid that supports the most functionality
        grid_supports_most = None
        num_supports_most = 0
        supports_most = []
        does_not_support_most = []
        for grid in ALL_GRIDS:
            num_supports = sum([grid in grids for grids, _ in answers.values()])
            if num_supports > num_supports_most:
                grid_supports_most = grid
                num_supports_most = num_supports
                supports_most = [question for question, (grids, _) in answers.items() if grid in grids]
                does_not_support_most = [question for question, (grids, _) in answers.items() if grid not in grids]

        grid_supports_second_most = None
        num_supports_second_most = 0
        supports_second_most = []
        does_not_support_second_most = []
        for grid in ALL_GRIDS:
            if grid == grid_supports_most:
                continue
            num_supports = sum([grid in grids for grids, _ in answers.values()])
            if num_supports > num_supports_second_most:
                grid_supports_second_most = grid
                num_supports_second_most = num_supports
                supports_second_most = [question for question, (grids, _) in answers.items() if grid in grids]
                does_not_support_second_most = [question for question, (grids, _) in answers.items() if grid not in grids]

        support_most_string = "\n - ".join(supports_most)
        does_not_support_most_string = "\n - ".join(does_not_support_most)
        support_second_most_string = "\n - ".join(supports_second_most)
        does_not_support_second_most_string = "\n - ".join(does_not_support_second_most)
        st.success(f"""The grid that supports the most functionality is {grid_supports_most}. It supports {num_supports_most} of the {len(answers)} features you're looking for.
                   
It supports:
- {support_most_string}

It does not support:
- {does_not_support_most_string}
""")

        st.warning(f"""The grid that supports the second most functionality is {grid_supports_second_most}. It supports {num_supports_second_most} of the {len(answers)} features you're looking for.

It supports:
- {support_second_most_string}

It does not support:
- {does_not_support_second_most_string}""")

    elif len(available_grids) == 1:
        reasons = "\n - ".join([reason for _, reason in answers.values()])
        st.success(f"""We reccomend {available_grids.pop()}! It's the best grid for your use case because: 
- {reasons}.""")
    else:
        reasons = "\n - ".join([reason for _, reason in answers.values()])
        st.success(f"""We recommend using {" or ".join(available_grids)}! They're the best grids for your use case because each:
- {reasons}.""")

