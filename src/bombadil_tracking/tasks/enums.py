class VALIDATION_PHASE:
    SMOKE_TEST = "Smoke Test"
    CHARACTERIZAION_NOMINAL = "Characterizaion (Nominal)"
    CHARACTERIZAION_EDGE = "Characterizaion (Edge)"
    RELIABILITY = "Reliability"
    FIELD = "Field"

    @staticmethod
    def as_list():
        return [
            value
            for name, value in vars(VALIDATION_PHASE).items()
            if not name.startswith("_")
            and not callable(value)
            and not isinstance(value, (staticmethod, classmethod, property, type))
        ]


class TASK_TYPE:
    VALIDATION = "Validation"
    DESIGN = "Design"
    REVIEW_FEEDBACK = "Review Feedback"
    MISC = "Miscellaneous"

    @staticmethod
    def as_list():
        return [
            value
            for name, value in vars(TASK_TYPE).items()
            if not name.startswith("_")
            and not callable(value)
            and not isinstance(value, (staticmethod, classmethod, property, type))
        ]
