--- 
title: "Writing games with Python and PsychoPy"
author: "Alexander (Sasha) Pastukhov"
date: "2021-11-15"
site: bookdown::bookdown_site
documentclass: book
bibliography: [book.bib]
url: https://alexander-pastukhov.github.io/writing-games-with-python-and-psychopy
# cover-image: path to the social sharing image like images/cover.jpg
description: |
  Material and exercises for 'Python for social and experimental psychology' seminar.
biblio-style: apalike
csl: chicago-fullnote-bibliography.csl
---

# Introduction {#intro}

This book will teach you programming. Hopefully, it will do so in a fun way because if there is something more satisfying than playing a video game then it is creating one. Although it is written for the course called *"Python for social and experimental psychology"*, my main aim is not to teach you Python per se. Python is a fantastic tool (more on this later) but it is just one of many programming languages that exist. My ultimate goal is to help you to develop general programming skills, which do not depend on a specific-programming language, and make sure that you form good habits that will make your code clear, easy to read, and easy to maintain. That last part is crucial. Programming is not about writing code that works. That, obviously, must be true but it is only the minimal requirement. Programming is about writing a clear and easy-to-read code that others and, even more importantly, you-two-weeks later can understand.

## Prerequisites
The material assumes no foreknowledge of Python or programming from the reader. Its purpose is to gradually build up your knowledge and allow you to create more and more complex games.

## Why games?
The actual purpose of this course is to teach psychology and social studies students how to program _experiments_. That is what the real research is about. However, there is little practical difference between the two. The basic ingredients are the same and, arguably, experiments are just boring games. And, be assured, if you can program a game, you can certainly program an experiment.

## Why should a psychologist learn programming?
Why should a psychologist, who is interested in people, learn how to program computers? The most obvious answer is that this is a useful skill. Being able to program gives you freedom to create an experiment that answers your research question, not an experiment that can be implemented given constraints of your software.

More importantly, at least from my point of view, learning how to program changes the way you think in general. People are smart but computers are dumb. When you explain your experiment or travel plans to somebody, you can be fairly vague, make a minor mistake, even skip certain parts. People are smart so they will fill the missing information in with their knowledge, spot and correct a mistake, ask you for more information, and can improvise on their own once they encounter something that you have not covered. Computers are dumb, so you must be precise, you cannot have gray areas, you cannot leave anything to "it will figure it out once it happens" (it won't). My personal experience, corroborated by psychologists who learned programming, is that it makes you realize just how vague and imprecise people can be without realizing it. Programming forces you to be precise and thorough, to plan ahead for any eventuality there might be. And this is a very useful skill by itself as it can be applied to any activity that requires planning be that an experimental design or travel arrangements.

## Why Python?
There are many ways to create an experiment for psychological research. You can use drag-and-drop systems either commercial like [Presentation](https://www.neurobs.com/), [Experiment Builder](https://www.sr-research.com/experiment-builder/) or free like [PsychoPy Bulder interface](https://psychopy.org/builder). They have a much shallower learning curve, so you can start creating and running your experiments faster. However, the simplicity of their use has a price: They are fairly limited in which stimuli you can use and how you can control the presentation schedule, conditions, feedback, etc. Typically, they allow you to extend them by programming the desired behavior but you do need to know how to program to do this (knowing Python supercharges your PsychoPy experiments). Thus, I think that while these systems, in particular [PsychoPy](https://psychopy.org/), are great tools to quickly bang a simple experiment together, they are most useful if you understand 
_how_ they create the underlying code and how you would program it yourself. Then, you will not be limited by the software, as you know you can program something the default drag-and-drop won't allow. At the same time, you can always opt in, if drag-and-drop is sufficient but faster. Or use a mix of the two approaches. At the end, it is about having options and creative freedom to program an experiment that will answer your research question, not an experiment that your software allows you to program.

We will learn programming in Python, which is a great language that combines simple and clear syntax with power and ability to tackle almost any problem. In this seminar, we will concentrate on desktop experiments but you can use it for online experiments ([oTree](https://otree.readthedocs.io/en/latest/) and [PsychoPy](https://psychopy.org/)), scientific programming ([NumPy](https://numpy.org/) and [SciPy](https://www.scipy.org/)), data analysis ([pandas](https://pandas.pydata.org/)), machine learning ([keras](https://keras.io/)), website programming ([django](https://www.djangoproject.com/)), computer vision ([OpenCV](https://opencv.org/)), etc. Thus, Python is one of the most versatile programming tools that you can use for all stages of your research or work. And, Python is free, so you do not need to worry whether you or your future employer will be able to afford license fees (a very real problem, if you use Matlab).

## Seminar-specific information
This is a material for _Python for social and experimental psychology_ seminar as taught by me at the University of Bamberg. Each chapter covers a single game, introducing necessary ideas and is accompanied by exercises that you need to complete and submit. To pass the seminar, you will need to complete all assignments, i.e., write all the games. You do not need to complete or provide correct solutions for _all_ the exercises to pass the course and information on how the points for exercises will be converted to an actual grade (if you need one) or "pass" will be available during the seminar.

The material is structured, so that each chapter or chapter section correspond to a single meeting. However, we are all different, so work at your own pace, read the material and submit assignments independently. I will provide detailed feedback for each assignment and you will have an opportunity to address issues and resubmit again with no loss of points. Note that my feedback will cover not only the actual problems with the code but the way you implemented the solution and how clean and well-documented your code is. Remember, our task is not just to learn how to program a working game but how to write a nice clear easy-to-read-and-maintain code^[Good habits! Form good habits! Thank you for reading this subliminal message.]. 

Very important: Do not hesitate to ask questions. If I feel that you missed the information in the material, I will point you to the exact location. If you are confused, I'll gently prod you with questions so that you will solve your own problem. If you need more information, I'll supply it. If you simply want to know more, ask and I'll explain why things are the way they are or suggest what to read. If I feel that you should be able to solve the issue without my help, I'll tell you so (although, I would still probably ask a few hinting questions).

## About the material
This material is **free to use** and is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives V4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
