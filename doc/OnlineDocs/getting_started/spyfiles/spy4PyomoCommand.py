"""
David L. Woodruff and Mingye Yang, Spring 2018
Code snippets for PyomoCommand.rst in testable form
"""

# @Troubleshooting_printed_command
>>> def ax_constraint_rule(model, i):
>>>     # return the expression for the constraint for i
>>>     print "ax_constraint_rule was called for i=",i
>>>     return sum(model.a[i,j] * model.x[j] for j in model.J) >= model.b[i]
>>>
>>> # the next line creates one constraint for each member of the set model.I
>>> model.AxbConstraint = Constraint(model.I, rule=ax_constraint_rule)
# @Troubleshooting_printed_command
