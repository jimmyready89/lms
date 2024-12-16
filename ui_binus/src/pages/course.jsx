import { useState } from 'react';
import { CourseCard } from '../widgets/cards/course-card';

const DataDummy = [
    {
        ID: 'Test',
        Title: 'Test',
        Score: 100,
    },
    {
        ID: 'Test',
        Title: 'Test',
        Score: 100,
    },
];

export function Course() {
    const [LECList, setLECList] = useState(DataDummy);
    const [LCList, setLCList] = useState(DataDummy);

    // setLECList(DataDummy);

    return (
        <>
            <h1 className="block antialiased tracking-normal font-sans text-xl font-semibold leading-snug text-blue-gray-900">
                LEC
            </h1>
            <div className="grid grid-cols-3 gap-3">
                {LECList.map((CourseData) => <CourseCard {...CourseData} />)}
            </div>
            <h1 className="block antialiased tracking-normal font-sans text-xl font-semibold leading-snug text-blue-gray-900">
                CL
            </h1>
            <div className="grid grid-cols-3 gap-4">
                {LCList.map((CourseData) => <CourseCard {...CourseData} />)}
            </div>
        </>
    );
}

export default Course;
