import React, { useMemo } from 'react'
import { useTable, usePagination } from 'react-table'
import MOCK_DATA from './MOCK_DATA.json'
import { COLUMNS } from './columns'
// import { ChevronDoubleLeftIcon, ChevronLeftIcon, ChevronRightIcon, ChevronDoubleRightIcon } from '@heroicons/react/solid'
import { Button, PageButton } from './shared/Button'

export const PaginationTable = () => {

    const columns = useMemo(() => COLUMNS, [])
    const data = useMemo(() => MOCK_DATA, [])

    // const tableInstance = useTable({
    //     columns,
    //     data
    // })
    // const tableInstance = useTable({
    //     columns : columns,
    //     data : data
    // })

    const {
        getTableProps,
        getTableBodyProps,
        headerGroups,    //array
        page,
        nextPage,
        previousPage,
        canNextPage,
        canPreviousPage,
        pageOptions,
        gotoPage,
        pageCount,
        setPageSize,
        state,
        prepareRow,
    } = useTable({
        columns,
        data,
        initialState: { pageIndex: 5 }
    },
        usePagination)

    const { pageIndex, pageSize } = state

    return (
        <>
            {/* <div className="mt-2 flex flex-col min-w-full">
                <div className="-my-2 overflow-x-auto -mx-4 sm:-mx-6 lg:-mx-8">
                    <div className="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
                        <div className="shadow-md overflow-hidden border-b border-gray-200 sm:rounded-xl flex flex-row">
                            <table {...getTableProps()} className="min-w=full divide-gray-200"> */}
            <div className="mt-2 flex flex-col">
                <div className="-my-2 overflow-x-auto -mx-4 sm:-mx-6 lg:-mx-8">
                    <div className="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
                        <div className="shadow overflow-hidden border-b border-gray-900 sm:rounded-lg">
                            <table {...getTableProps()} className="table-auto min-w-full divide-y divide-gray-200">
                                <thead className="bg-gray-300">
                                    {headerGroups.map((headerGroup) => (
                                        <tr {...headerGroup.getHeaderGroupProps()}>
                                            {headerGroup.headers.map((column) => (
                                                <th {...column.getHeaderProps()} className="px-6 py-3 text-left text-s font-medium font-bold text-gray-500 uppercase tracking-wider">
                                                    {column.render('Header')}
                                                </th>
                                            ))}

                                        </tr>
                                    ))}
                                </thead>
                                <tbody {...getTableBodyProps()} className="bg-white divide-y divide-gray-200">
                                    {
                                        page.map((row) => {
                                            prepareRow(row)
                                            return (
                                                <tr {...row.getRowProps()} className="even:bg-gray-100">
                                                    {row.cells.map((cell) => {
                                                        return (
                                                            <td {...cell.getCellProps()} className="px-6 py-4 whitespace-nowrap">
                                                                {cell.render('Cell')}
                                                            </td>
                                                        )
                                                    })}

                                                </tr>
                                            )
                                        })
                                    }
                                </tbody>
                            </table>
                            <div className="py-3 flex items-center justify-between">
                                <div className="flex-1 flex justify-between sm:hidden">
                                    <button onClick={() => gotoPage(0)} disabled={!canPreviousPage}>
                                        {'<<'}
                                    </button>{' '}
                                    <button onClick={() => previousPage()} disabled={!canPreviousPage}>
                                        Previous
                                    </button>{' '}
                                    <button onClick={() => nextPage()} disabled={!canNextPage}>
                                        Next
                                    </button>{' '}
                                    <button onClick={() => gotoPage(pageCount - 1)} disabled={!canNextPage}>
                                        {'>>'}
                                    </button>{' '}
                                    {' '}
                                    <div className="flex gap-x-2">
                                        <span>
                                            Page{' '}
                                            <strong>
                                                {pageIndex + 1} of {pageOptions.length}
                                            </strong>{' '}
                                        </span>
                                        <span>
                                            | Go to page:{' '}

                                            <input
                                                type='number'
                                                defaultValue={pageIndex + 1}
                                                onChange={e => {
                                                    const pageNumber = e.target.value ? Number(e.target.value) - 1 : 0
                                                    gotoPage(pageNumber)
                                                }}
                                                style={{ width: '50px' }}
                                            />
                                        </span>{' '}
                                        <select value={pageSize} onChange={e => setPageSize(Number(e.target.value))}>
                                            {[10, 25, 50].map(pageSize => (
                                                <option key={pageSize} value={pageSize}>
                                                    Show {pageSize}
                                                </option>
                                            ))}
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}
