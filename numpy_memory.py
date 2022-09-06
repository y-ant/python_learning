import numpy as np
import time


def matrix_stats(matrix, sum_horizontally, optional_text = ''):

    if sum_horizontally == True:
        sum_horizontally = 1
        text = 'horizontally'
    else:
        sum_horizontally = 0
        text = 'vertically'

    matrix_description = "row(s)"
    if matrix.shape[0] > matrix.shape[1]:
        matrix_description = "column(s)"
    print('--' * 20)

    print('matrix shape', matrix.shape, ' i.e. matrix with longer', matrix_description)

    if (matrix.flags['C_CONTIGUOUS'] == True) and (matrix.flags['F_CONTIGUOUS'] == False):
        print('Memory setup: Row major.')
    elif (matrix.flags['C_CONTIGUOUS'] == False) and (matrix.flags['F_CONTIGUOUS'] == True):
        print('Memory setup: Column major.')
    else:
        print('Memory setup weird.')
        print('C_CONTIGUOUS:', matrix.flags['C_CONTIGUOUS'])
        print('F_CONTIGUOUS:', matrix.flags['F_CONTIGUOUS'])
    print('Memory setup: ',optional_text)
    print('-' * 20)

    ts = time.time()
    for i in range(1000):
        matrix.sum(axis=sum_horizontally)
    print("(example of results:", matrix.sum(axis=sum_horizontally), ')')
    print('summation time: ', time.time() - ts, ', sumation done ', text)
    print('--' * 20)


long_array = 100 * 1000

m2 = np.random.rand(long_array * 2)

m2_row_major_longer_rows = m2.reshape(2, long_array, order="C")
m2_column_major_longer_rows = m2.reshape(2, long_array, order="F")
m2_default_longer_rows = m2.reshape(2, long_array)

m2_row_major_longer_columns = m2.reshape(long_array, 2, order="C")
m2_column_major_longer_columns = m2.reshape(long_array, 2, order="F")
m2_default_longer_columns = m2.reshape(long_array, 2)

print("LONGER ROWS MATRICES. DIFFERENT MEMORY SETUPS")
matrix_stats(m2_default_longer_rows, sum_horizontally=True)
# matrix_stats(m2_row_major_longer_rows, sum_horizontally=True, optional_text='Should be Row major')
# matrix_stats(m2_column_major_longer_rows, sum_horizontally=True, optional_text='Should be Column major')

print("LONGER COLUMNS MATRICES. DIFFERENT MEMORY SETUPS")
matrix_stats(m2_default_longer_columns, sum_horizontally=False)
# matrix_stats(m2_row_major_longer_columns, sum_horizontally=False, optional_text='Should be Row major')
# matrix_stats(m2_column_major_longer_columns, sum_horizontally=False, optional_text='Should be Column major')
print('#####' * 10)
 