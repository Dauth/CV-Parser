from Match import Match
from MatchBox import MatchBox
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from Facade import Facade
from InformationNode import InformationNode

class Matcher(object):
    db = None

    def __init__(self, db):
        self.db = db


    def match(self, resume, job):
        imptKeywordSet = set(InformationNode.convertStringIntoList(job.getImptKeywords()))
        print(imptKeywordSet)
        rskillSet = set(resume.getSkills())
        jskillSet = set(job.getSkills())
        resultSkillSet = rskillSet.intersection(jskillSet)
        resultSkillSet2 = rskillSet.intersection(imptKeywordSet)
        # print(rskillSet)
        # print(jskillSet)
        resultSkill = (len(resultSkillSet) + len(resultSkillSet2))
        rLangSet = set(resume.getLanguage())
        jLangSet = set(job.getLanguage())
        resultLangSet = rLangSet.intersection(jLangSet)
        resultLangSet2 = rskillSet.intersection(imptKeywordSet)
        # print(rLangSet)
        # print(jLangSet)
        resultLang = (len(resultLangSet) + len(resultLangSet2))
        rLocationSet = resume.getLocation().getCountry()
        jLocationSet = job.getLocation().getCountry()
        resultLocationSet = int(rLocationSet == jLocationSet)
        print(resultLocationSet)

        # print(resumeNode.getEducation())
        # print(jobNode.getEducation())
        eduResult = (self.compareEducationBetweenJobandResume(resume.getEducation(), job.getEducation()))
        expResult = (self.compareExperienceBetweenJobandResume(resume.getExperience(), job.getExperience(),InformationNode.convertStringIntoList(job.getImptKeywords())))
        finalResult = eduResult + expResult +resultLocationSet + resultLang + resultSkill
        new_match = Match(resume, job, finalResult)
        return new_match

    def matchAll(self, mode = 0):

        #Both new resumes and new jobs are uploaded
        if mode == 0:
            resume_list = self.db.getNewResumes()
            job_list = self.db.getNewJobs()
            boxes = set()

            for job in job_list:
                box = MatchBox(job)
                for resume in resume_list:
                    new_match = self.match(resume, job)
                    box.addMatch(new_match)
                boxes.add(box)
            self.db.addMatchBoxes(boxes)

        #Only new resumes are uploaded
        elif mode == 1:
            resume_list = self.db.getNewResumes()
            boxes = self.db.getMatchBoxes()

            for b in boxes:
                box = b
                for resume in resume_list:
                    job = box.getJob()
                    new_match = self.match(resume, job)
                    box.addMatch(new_match)
                boxes.add(box)
            self.db.storeMatchBoxes(boxes)

        #Only new jobs are uploaded
        elif mode == 2:
            resume_list = self.db.getAllResumes()
            job_list = self.db.getNewJobs()
            boxes = set()

            for job in job_list:
                box = MatchBox(job)
                for resume in resume_list:
                    new_match = self.match(resume, job)
                    box.addMatch(new_match)
                boxes.add(box)
            self.db.addMatchBoxes(boxes)

        else:
            return False

    def compareEducationBetweenJobandResume(self, resumeEdu, jobEdu):
        for key in jobEdu:
            eduType = key.split('in')[0].strip()
            eduArea = key.split('in')[1].strip()
            for keyN in resumeEdu:
                if eduArea in keyN and eduType in keyN:
                    return 1
        return 0

    def compareExperienceBetweenJobandResume(self, resumeExp, jobExp, imptkeywords):
        resumeSet =set(i.getWorkPositionOrExp() for i in resumeExp)
        jobSet =set(i.getWorkPositionOrExp() for i in jobExp)
        imptkeywordsSet = set(imptkeywords)
        return len(resumeSet.intersection(jobSet)) + len(resumeSet.intersection(imptkeywordsSet))