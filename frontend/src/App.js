import { SortingTable } from './components/SortingTable'
import { FilteringTable } from './components/FilteringTable'
import { PaginationTable } from './components/PaginationTable';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 text-gray-900">
      <main className="max-w-full mx-auto px-4 sm:px-6 lg:px-8 pt-4">
        <div className="">
          <h1 className="text-xl font-semibold">React Table + Tailwind CSS != ❤</h1>
        </div>
        <div className="mt-4">
          <PaginationTable />
        </div>
      </main>
    </div>
  );
}

export default App;
