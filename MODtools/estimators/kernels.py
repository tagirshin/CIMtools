# -*- coding: utf-8 -*-
#
#  Copyright 2016 Ramil Nugmanov <stsouko@live.ru>
#  This file is part of MODtools.
#
#  MODtools is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
import numpy as np


def tanimoto_kernel(x, y):
    x_dot = np.dot(x, y.T)

    x2 = (x**2).sum(axis=1)
    y2 = (y**2).sum(axis=1)

    len_x2 = len(x2)
    len_y2 = len(y2)

    result = x_dot / (np.array([x2] * len_y2).T + np.array([y2] * len_x2) - x_dot)
    result[np.isnan(result)] = 0

    return result
