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
        # print(imptKeywordSet)
        eduResult = 0
        expResult = 0
        resultLocationSet = 0
        resultLang = 0
        resultSkill = 0
        matchedKeywords = []

        if(resume.isSkillsPresent() and job.isSkillsPresent()):
            rskillSet = set(resume.getSkills())
            jskillSet = set(job.getSkills())
            resultSkillSet = rskillSet.intersection(jskillSet)
            resultSkillSet2 = rskillSet.intersection(imptKeywordSet)
            resultSkill = (len(resultSkillSet) + len(resultSkillSet2))
            self.mergeSetIntoList(matchedKeywords, resultSkillSet.union(resultSkillSet2))
            # print(rskillSet)
            # print(jskillSet)

        if(resume.isLanguagePresent() and job.isLanguagePresent()):
            rLangSet = set(resume.getLanguage())
            jLangSet = set(job.getLanguage())
            resultLangSet = rLangSet.intersection(jLangSet)
            resultLangSet2 = jLangSet.intersection(imptKeywordSet)
            resultLang = (len(resultLangSet) + len(resultLangSet2))
            self.mergeSetIntoList(matchedKeywords, resultLangSet.union(resultLangSet2))
            # print(rLangSet)
            # print(jLangSet)

        if (resume.isLocationPresent()  and job.isLocationPresent()):
            rLocationSet = resume.getLocation().getCountry()
            jLocationSet = job.getLocation().getCountry()
            resultLocationSet = int(rLocationSet == jLocationSet)
            # print(resultLocationSet)

        if(resume.isEducationPresent() and job.isEducationPresent()):
            eduResult = (self.compareEducationBetweenJobandResume(resume.getEducation(), job.getEducation()))
            # print(resumeNode.getEducation())
            # print(jobNode.getEducation())
        if(resume.isExperiencePresent() and job.isExperiencePresent()):
            expResult = (self.compareExperienceBetweenJobandResume(resume.getExperience(), job.getExperience(),InformationNode.convertStringIntoList(job.getImptKeywords()), matchedKeywords))


        finalResult = eduResult + expResult +resultLocationSet + resultLang + resultSkill

        new_match = Match(resume, job, finalResult, matchedKeywords)
        print(finalResult)
        print(new_match.getMatchedKeyWords())
        return new_match

    def matchAll(self, mode = 0):

        #Both new resumes and new jobs are uploaded
        if mode == 0:
            resume_list = self.db.getNewResumes()
            job_list = self.db.getNewJobs()
            boxes = set()

            assert len(job_list) > 0
            assert len(resume_list) > 0
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

            assert len(resume_list) > 0
            assert len(boxes) > 0
            for b in boxes:
                box = b
                for resume in resume_list:
                    job = box.getJob()
                    new_match = self.match(resume, job)
                    box.addMatch(new_match)
            self.db.storeMatchBoxes(boxes)

        #Only new jobs are uploaded
        elif mode == 2:
            resume_list = self.db.getAllResumes()
            job_list = self.db.getNewJobs()
            boxes = set()

            assert len(job_list) > 0
            assert len(resume_list) > 0
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

    def compareExperienceBetweenJobandResume(self, resumeExp, jobExp, imptkeywords, matchedKeywords):
        resumeSet =set(i.getWorkPositionOrExp() for i in resumeExp)
        jobSet =set(i.getWorkPositionOrExp() for i in jobExp)
        imptkeywordsSet = set(imptkeywords)
        self.mergeSetIntoList(matchedKeywords, resumeSet.intersection(jobSet))
        self.mergeSetIntoList(matchedKeywords, resumeSet.intersection(imptkeywordsSet))
        return len(resumeSet.intersection(jobSet)) + len(resumeSet.intersection(imptkeywordsSet))

    def mergeSetIntoList(self, matchedKeywords, set1):
        for i in set1:
            if i not in matchedKeywords:
                matchedKeywords.append(i)