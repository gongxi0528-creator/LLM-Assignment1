#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import React, { useMemo, useState } from "react";
import { motion } from "framer-motion";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Slider } from "@/components/ui/slider";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
} from "recharts";
import { Briefcase, GraduationCap, Languages, MapPin, Mail, Phone, Trophy } from "lucide-react";

export default function XiGongResumeApp() {
  const [focusArea, setFocusArea] = useState("analytics");
  const [skillLevel, setSkillLevel] = useState([75]);
  const [showEducation, setShowEducation] = useState(true);
  const [showLeadership, setShowLeadership] = useState(true);
  const [showInterests, setShowInterests] = useState(true);

  const profile = {
    name: "Xi Gong",
    title: "Financial Analyst | Management Analytics Candidate",
    phone: "+1 (647) 831-4670",
    email: "george.gong@rotman.utoronto.ca",
    location: "Toronto, ON",
    summary:
      "Financial analyst with experience in financial reporting, reconciliation, tax support, and cross-platform data analysis. Strong exposure to SAP, BlackLine, Vertex, Excel, Power BI, Python, R, and SQL, with a growing focus on analytics-driven decision making in finance.",
  };

  const education = [
    {
      program: "Master of Management Analytics",
      school: "Rotman School of Management, University of Toronto",
      period: "Aug 2025 – Present",
      details: "Graduate study focused on analytics, business problem solving, and quantitative decision-making.",
    },
    {
      program: "Bachelor of Business Administration",
      school: "University of Toronto",
      period: "Sep 2020 – Jun 2025",
      details: "Specialist Co-op in Management and Finance | GPA: 3.73/4 | Dean’s List (2021–2025).",
    },
  ];

  const experience = [
    {
      company: "Johnson & Johnson Canada",
      role: "Tax Analyst",
      period: "Jan 2024 – Sep 2024",
      months: 9,
      category: "finance",
      highlights: [
        "Collected, consolidated, and analyzed financial data across SAP, BlackLine, and LYNX for annual reporting with 100% accuracy.",
        "Prepared monthly tax reports using Vertex and reconciled 300+ data points for compliance and audit readiness.",
        "Coordinated with CRA, educational institutions, and internal US finance teams to support timely information exchange.",
      ],
    },
    {
      company: "Dome Productions",
      role: "General Accountant",
      period: "Aug 2022 – Jun 2023",
      months: 11,
      category: "operations",
      highlights: [
        "Entered and verified 100+ crew sheets to support invoice accuracy, reconciliation, and expense processing.",
        "Prepared monthly financial reports in SAP to support accounting and financial analysis workflows.",
        "Created a 20-page training manual that improved intern onboarding and platform adoption.",
      ],
    },
    {
      company: "Calian x RBAC Case Competition",
      role: "Team Leader – 2nd Place",
      period: "Oct 2025 – Nov 2025",
      months: 2,
      category: "analytics",
      highlights: [
        "Led a team of four using K-means clustering and classification models including KNN, Logistic Regression, Random Forest, and XGBoost.",
        "Translated analytical findings into business recommendations focused on churn reduction and restaurant performance.",
        "Delivered a 10-minute presentation and handled judge Q&A with strong clarity and persuasion.",
      ],
    },
  ];

  const skills = [
    { skill: "Excel", proficiency: 88, area: "finance" },
    { skill: "Financial Analysis", proficiency: 84, area: "finance" },
    { skill: "SAP", proficiency: 80, area: "finance" },
    { skill: "Python", proficiency: 78, area: "analytics" },
    { skill: "SQL", proficiency: 74, area: "analytics" },
    { skill: "R", proficiency: 70, area: "analytics" },
    { skill: "Power BI", proficiency: 72, area: "analytics" },
    { skill: "BlackLine", proficiency: 76, area: "operations" },
    { skill: "Reconciliation", proficiency: 86, area: "operations" },
    { skill: "DCF Modeling", proficiency: 68, area: "finance" },
  ];

  const filteredSkills = useMemo(() => {
    return skills.filter(
      (s) => (focusArea === "all" || s.area === focusArea) && s.proficiency >= skillLevel[0]
    );
  }, [focusArea, skillLevel]);

  const radarData = useMemo(() => {
    const buckets = {
      finance: [88, 84, 80, 68],
      analytics: [78, 74, 70, 72],
      operations: [76, 86],
    };

    return [
      {
        subject: "Finance",
        value: Math.round(buckets.finance.reduce((a, b) => a + b, 0) / buckets.finance.length),
      },
      {
        subject: "Analytics",
        value: Math.round(buckets.analytics.reduce((a, b) => a + b, 0) / buckets.analytics.length),
      },
      {
        subject: "Operations",
        value: Math.round(buckets.operations.reduce((a, b) => a + b, 0) / buckets.operations.length),
      },
      { subject: "Communication", value: 85 },
      { subject: "Leadership", value: 82 },
    ];
  }, []);

  const totalMonths = experience.reduce((sum, item) => sum + item.months, 0);

  const statCards = [
    { label: "Professional Roles", value: "2" },
    { label: "Case Competitions", value: "1" },
    { label: "Documented Data Points Reconciled", value: "300+" },
    { label: "Total Experience Window", value: `${totalMonths} mo` },
  ];

  return (
    <div className="min-h-screen bg-slate-50 p-6 md:p-10">
      <div className="mx-auto max-w-7xl space-y-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="grid gap-6 lg:grid-cols-[1.3fr_0.7fr]"
        >
          <Card className="rounded-3xl border-0 shadow-lg">
            <CardHeader className="pb-4">
              <div className="flex flex-col gap-4 md:flex-row md:items-start md:justify-between">
                <div className="space-y-2">
                  <CardTitle className="text-3xl font-bold tracking-tight">{profile.name}</CardTitle>
                  <CardDescription className="text-base text-slate-600">
                    {profile.title}
                  </CardDescription>
                  <p className="max-w-3xl text-sm leading-6 text-slate-700">{profile.summary}</p>
                </div>
                <div className="grid gap-2 text-sm text-slate-700">
                  <div className="flex items-center gap-2"><Phone className="h-4 w-4" /> {profile.phone}</div>
                  <div className="flex items-center gap-2"><Mail className="h-4 w-4" /> {profile.email}</div>
                  <div className="flex items-center gap-2"><MapPin className="h-4 w-4" /> {profile.location}</div>
                </div>
              </div>
            </CardHeader>
            <CardContent>
              <div className="flex flex-wrap gap-2">
                <Badge className="rounded-full px-3 py-1">Finance</Badge>
                <Badge className="rounded-full px-3 py-1" variant="secondary">Analytics</Badge>
                <Badge className="rounded-full px-3 py-1" variant="outline">Reporting</Badge>
                <Badge className="rounded-full px-3 py-1" variant="outline">Reconciliation</Badge>
                <Badge className="rounded-full px-3 py-1" variant="secondary">Data Analysis</Badge>
              </div>
            </CardContent>
          </Card>

          <Card className="rounded-3xl border-0 shadow-lg">
            <CardHeader>
              <CardTitle className="text-xl">Interactive Controls</CardTitle>
              <CardDescription>Change the view to tailor the resume dashboard.</CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="space-y-2">
                <label className="text-sm font-medium">Focus area</label>
                <Select value={focusArea} onValueChange={setFocusArea}>
                  <SelectTrigger className="rounded-2xl">
                    <SelectValue placeholder="Choose a focus" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="all">All</SelectItem>
                    <SelectItem value="finance">Finance</SelectItem>
                    <SelectItem value="analytics">Analytics</SelectItem>
                    <SelectItem value="operations">Operations</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <label className="text-sm font-medium">Minimum skill score</label>
                  <span className="text-sm text-slate-500">{skillLevel[0]}</span>
                </div>
                <Slider value={skillLevel} onValueChange={setSkillLevel} min={60} max={90} step={2} />
              </div>

              <div className="space-y-3">
                <div className="flex items-center space-x-2">
                  <Checkbox id="education" checked={showEducation} onCheckedChange={(v) => setShowEducation(Boolean(v))} />
                  <label htmlFor="education" className="text-sm">Show education</label>
                </div>
                <div className="flex items-center space-x-2">
                  <Checkbox id="leadership" checked={showLeadership} onCheckedChange={(v) => setShowLeadership(Boolean(v))} />
                  <label htmlFor="leadership" className="text-sm">Show leadership</label>
                </div>
                <div className="flex items-center space-x-2">
                  <Checkbox id="interests" checked={showInterests} onCheckedChange={(v) => setShowInterests(Boolean(v))} />
                  <label htmlFor="interests" className="text-sm">Show languages & interests</label>
                </div>
              </div>

              <Button className="w-full rounded-2xl">Resume Snapshot Ready</Button>
            </CardContent>
          </Card>
        </motion.div>

        <div className="grid gap-4 md:grid-cols-4">
          {statCards.map((stat, idx) => (
            <motion.div
              key={stat.label}
              initial={{ opacity: 0, y: 16 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.35, delay: idx * 0.06 }}
            >
              <Card className="rounded-3xl border-0 shadow-sm">
                <CardContent className="p-5">
                  <div className="text-2xl font-bold">{stat.value}</div>
                  <div className="mt-1 text-sm text-slate-600">{stat.label}</div>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>

        <div className="grid gap-6 xl:grid-cols-[1.1fr_0.9fr]">
          <Card className="rounded-3xl border-0 shadow-lg">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-xl"><Briefcase className="h-5 w-5" /> Experience</CardTitle>
              <CardDescription>Role history personalized from Xi Gong’s resume.</CardDescription>
            </CardHeader>
            <CardContent className="space-y-5">
              {experience
                .filter((item) => focusArea === "all" || item.category === focusArea)
                .map((item) => (
                  <div key={`${item.company}-${item.role}`} className="rounded-2xl border border-slate-200 p-4">
                    <div className="flex flex-col gap-2 md:flex-row md:items-center md:justify-between">
                      <div>
                        <div className="font-semibold text-slate-900">{item.role}</div>
                        <div className="text-sm text-slate-600">{item.company}</div>
                      </div>
                      <Badge variant="outline" className="w-fit rounded-full">{item.period}</Badge>
                    </div>
                    <ul className="mt-3 space-y-2 text-sm leading-6 text-slate-700">
                      {item.highlights.map((point) => (
                        <li key={point}>• {point}</li>
                      ))}
                    </ul>
                  </div>
                ))}
            </CardContent>
          </Card>

          <Card className="rounded-3xl border-0 shadow-lg">
            <CardHeader>
              <CardTitle className="text-xl">Experience Timeline</CardTitle>
              <CardDescription>Months represented by each role or project experience.</CardDescription>
            </CardHeader>
            <CardContent className="h-[360px] pt-2">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={experience.filter((item) => focusArea === "all" || item.category === focusArea)}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="role" tick={{ fontSize: 12 }} interval={0} angle={-12} textAnchor="end" height={70} />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="months" radius={[10, 10, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </div>

        <div className="grid gap-6 xl:grid-cols-[1fr_1fr]">
          <Card className="rounded-3xl border-0 shadow-lg">
            <CardHeader>
              <CardTitle className="text-xl">Skills Table</CardTitle>
              <CardDescription>Filtered using the interactive controls above.</CardDescription>
            </CardHeader>
            <CardContent>
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Skill</TableHead>
                    <TableHead>Area</TableHead>
                    <TableHead className="text-right">Score</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {filteredSkills.map((row) => (
                    <TableRow key={row.skill}>
                      <TableCell className="font-medium">{row.skill}</TableCell>
                      <TableCell className="capitalize">{row.area}</TableCell>
                      <TableCell className="text-right">{row.proficiency}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </CardContent>
          </Card>

          <Card className="rounded-3xl border-0 shadow-lg">
            <CardHeader>
              <CardTitle className="text-xl">Capability Mix</CardTitle>
              <CardDescription>Summary of Xi Gong’s skill profile across core dimensions.</CardDescription>
            </CardHeader>
            <CardContent className="h-[360px] pt-2">
              <ResponsiveContainer width="100%" height="100%">
                <RadarChart data={radarData} outerRadius="72%">
                  <PolarGrid />
                  <PolarAngleAxis dataKey="subject" />
                  <PolarRadiusAxis domain={[0, 100]} />
                  <Radar dataKey="value" fillOpacity={0.35} />
                  <Tooltip />
                </RadarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </div>

        {showEducation && (
          <Card className="rounded-3xl border-0 shadow-lg">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-xl"><GraduationCap className="h-5 w-5" /> Education</CardTitle>
            </CardHeader>
            <CardContent className="grid gap-4 md:grid-cols-2">
              {education.map((item) => (
                <div key={item.program} className="rounded-2xl border border-slate-200 p-4">
                  <div className="font-semibold">{item.program}</div>
                  <div className="text-sm text-slate-600">{item.school}</div>
                  <div className="mt-1 text-sm text-slate-500">{item.period}</div>
                  <p className="mt-3 text-sm leading-6 text-slate-700">{item.details}</p>
                </div>
              ))}
            </CardContent>
          </Card>
        )}

        <div className="grid gap-6 lg:grid-cols-2">
          {showLeadership && (
            <Card className="rounded-3xl border-0 shadow-lg">
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-xl"><Trophy className="h-5 w-5" /> Leadership & Achievement</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="rounded-2xl border border-slate-200 p-4 text-sm leading-6 text-slate-700">
                  <div className="font-semibold text-slate-900">2025 Calian x RBAC Case Competition — 2nd Place</div>
                  <p className="mt-2">
                    Led a team of four to segment customers with K-means clustering and build a churn prediction solution using KNN,
                    Logistic Regression, Random Forest, and XGBoost.
                  </p>
                  <p className="mt-2">
                    Framed recommendations around customer retention and restaurant performance, then delivered the final presentation
                    and answered judges’ questions in Q&A.
                  </p>
                </div>
              </CardContent>
            </Card>
          )}

          {showInterests && (
            <Card className="rounded-3xl border-0 shadow-lg">
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-xl"><Languages className="h-5 w-5" /> Languages & Interests</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4 text-sm text-slate-700">
                <div>
                  <div className="font-semibold text-slate-900">Languages</div>
                  <p className="mt-2">Native Chinese, Professional English, Basic French, Basic Cantonese</p>
                </div>
                <div>
                  <div className="font-semibold text-slate-900">Interests</div>
                  <p className="mt-2">
                    Value investing, U.S. stock market research, reading Poor Charlie’s Almanack, and following basketball.
                  </p>
                </div>
              </CardContent>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
}

