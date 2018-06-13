# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    setup.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 21:22:52 by kcosta           #+#    #+#              #
#    Updated: 2018/06/13 22:20:30 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from setuptools import setup, find_packages

with open('README.md') as f:
  readme = f.read()

setup(
  name='expert_system',
  version='0.1',
  description=readme,
  author='kcosta',
  author_email='kcosta@student.42.fr',
  url='https://github.com/kcosta42/Expert-System',
  license='MIT',
  packages=find_packages(exclude=('tests', 'docs'))
)
